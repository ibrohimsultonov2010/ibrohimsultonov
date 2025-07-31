from django.contrib import admin
from django.utils.html import format_html
from .models import PersonalInfo, Skill, Project, Experience, Education, Contact, ChatMessage, SocialLink, ProjectImage, Certificate

# Admin panel sarlavhasi
admin.site.site_header = "Portfolio Boshqaruvi"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Portfolio boshqaruvi paneliga xush kelibsiz"

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'profile_image_preview', 'created_at']
    search_fields = ['name', 'title', 'email']
    readonly_fields = ['profile_image_preview']
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('name', 'title', 'description', 'email', 'phone', 'location')
        }),
        ('Ijtimoiy tarmoqlar', {
            'fields': ('github', 'linkedin', 'twitter'),
            'classes': ('collapse',)
        }),
        ('Profil rasmi', {
            'fields': ('profile_image', 'profile_image_preview'),
            'description': 'Dumaloq profil rasmini yuklang. Tavsiya etilgan o\'lcham: 400x400 piksel'
        }),
    )
    inlines = [SocialLinkInline]
    
    def profile_image_preview(self, obj):
        if obj.profile_image:
            return f'<img src="{obj.profile_image.url}" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover;" />'
        return "Rasm yuklanmagan"
    profile_image_preview.short_description = "Profil rasmi"
    profile_image_preview.allow_tags = True

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category', 'order']
    
    def get_list_display(self, request):
        return ['name', 'category', 'proficiency', 'order']
    
    def get_list_filter(self, request):
        return ['category']
    
    def get_search_fields(self, request):
        return ['name']

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'featured', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    prepopulated_fields = {'title': ('title',)}
    
    def get_list_display(self, request):
        return ['title', 'technologies', 'featured', 'created_at']
    
    def get_list_filter(self, request):
        return ['featured', 'created_at']
    
    def get_search_fields(self, request):
        return ['title', 'description', 'technologies']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'start_date']
    search_fields = ['position', 'company', 'description']
    ordering = ['-start_date']
    
    def get_list_display(self, request):
        return ['position', 'company', 'start_date', 'end_date', 'current']
    
    def get_list_filter(self, request):
        return ['current', 'start_date']
    
    def get_search_fields(self, request):
        return ['position', 'company', 'description']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'field_of_study', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'start_date']
    search_fields = ['degree', 'institution', 'field_of_study']
    
    def get_list_display(self, request):
        return ['degree', 'institution', 'field_of_study', 'start_date', 'end_date', 'current']
    
    def get_list_filter(self, request):
        return ['current', 'start_date']
    
    def get_search_fields(self, request):
        return ['degree', 'institution', 'field_of_study']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    actions = ['mark_as_read']
    
    def get_list_display(self, request):
        return ['name', 'email', 'subject', 'created_at', 'read']
    
    def get_list_filter(self, request):
        return ['read', 'created_at']
    
    def get_search_fields(self, request):
        return ['name', 'email', 'subject', 'message']
    
    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Tanlangan xabarlarni o'qilgan deb belgilash"

admin.site.register(ChatMessage)
admin.site.unregister(PersonalInfo)
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(SocialLink)
admin.site.unregister(Project)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'image_preview', 'order']
    search_fields = ['title', 'description']
    list_filter = ['date']
    readonly_fields = ['image_preview']
    ordering = ['-date', 'order']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:60px; height:60px; object-fit:contain; border-radius:12px;" />', obj.image.url)
        return "Rasm yo'q"
    image_preview.short_description = "Sertifikat rasmi"
    image_preview.allow_tags = True
