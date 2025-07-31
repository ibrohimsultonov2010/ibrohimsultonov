from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import PersonalInfo, Skill, Project, Experience, Education, Contact, ChatMessage, Certificate
from .forms import ContactForm

# Create your views here.

def home(request):
    """Ana sahifa - portfolio"""
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    skills = Skill.objects.all()
    projects = Project.objects.filter(featured=True)[:6]
    experiences = Experience.objects.all()[:5]
    education = Education.objects.all()[:3]
    
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'education': education,
    }
    return render(request, 'app/home.html', context)

def about(request):
    """Haqida sahifasi"""
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    certificates = Certificate.objects.all()
    
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'experiences': experiences,
        'education': education,
        'certificates': certificates,
    }
    return render(request, 'app/about.html', context)

def projects(request):
    """Loyihalar sahifasi"""
    projects = Project.objects.all()
    
    context = {
        'projects': projects,
    }
    return render(request, 'app/projects.html', context)

def contact(request):
    """Aloqa sahifasi"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Xabar muvaffaqiyatli yuborildi!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    context = {
        'form': form,
        'personal_info': personal_info,
    }
    return render(request, 'app/contact.html', context)

def contact_ajax(request):
    """AJAX orqali aloqa formasi"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Xabar muvaffaqiyatli yuborildi!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Noto\'g\'ri so\'rov'})

def chat_room(request):
    if request.method == "POST":
        username = request.POST.get("username", "Anonim")
        message = request.POST.get("message")
        if message:
            ChatMessage.objects.create(username=username, message=message)
        return redirect("chat_room")
    messages = ChatMessage.objects.order_by("-timestamp")[:50][::-1]
    return render(request, "app/chat_room.html", {"messages": messages})

def chat_api(request):
    if request.method == "POST":
        username = request.POST.get("username", "Anonim")
        message = request.POST.get("message")
        if message:
            ChatMessage.objects.create(username=username, message=message)
            return JsonResponse({"status": "ok"})
        return JsonResponse({"status": "error", "msg": "Xabar bo'sh bo'lishi mumkin emas"})
    else:
        messages = ChatMessage.objects.order_by("-timestamp")[:50][::-1]
        data = [
            {"username": m.username, "message": m.message, "timestamp": m.timestamp.strftime("%H:%M:%S")} for m in messages
        ]
        return JsonResponse({"messages": data})
