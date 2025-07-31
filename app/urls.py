from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('contact/ajax/', views.contact_ajax, name='contact_ajax'),
    path('chat/', views.chat_room, name='chat_room'),
    path('chat/api/', views.chat_api, name='chat_api'),
] 