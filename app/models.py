from django.db import models

# Create your models here.

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    title = models.CharField(max_length=200, verbose_name="Lavozim")
    description = models.TextField(verbose_name="Tavsif")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    location = models.CharField(max_length=100, verbose_name="Manzil")
    github = models.URLField(blank=True, verbose_name="GitHub")
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn")
    twitter = models.URLField(blank=True, verbose_name="Twitter")
    profile_image = models.ImageField(upload_to='profile/', blank=True, verbose_name="Profil rasmi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    
    class Meta:
        verbose_name = "Shaxsiy ma'lumot"
        verbose_name_plural = "Shaxsiy ma'lumotlar"
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Dasturlash tillari'),
        ('framework', 'Framework va kutubxonalar'),
        ('database', 'Ma\'lumotlar bazalari'),
        ('tool', 'Asboblar va texnologiyalar'),
        ('soft', 'Yumshoq ko\'nikmalar'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Nomi")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Kategoriya")
    proficiency = models.IntegerField(help_text="Ko'nikma darajasi 1-100 oralig'ida", verbose_name="Daraja")
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome ikon sinfi", verbose_name="Ikon")
    order = models.IntegerField(default=0, verbose_name="Tartib")
    
    class Meta:
        verbose_name = "Ko'nikma"
        verbose_name_plural = "Ko'nikmalar"
        ordering = ['category', 'order']
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nomi")
    description = models.TextField(verbose_name="Tavsif")
    image = models.ImageField(upload_to='projects/', blank=True, verbose_name="Rasm")
    technologies = models.CharField(max_length=300, help_text="Vergul bilan ajratilgan texnologiyalar ro'yxati", verbose_name="Texnologiyalar")
    github_url = models.URLField(blank=True, verbose_name="GitHub havolasi")
    live_url = models.URLField(blank=True, verbose_name="Jonli havola")
    featured = models.BooleanField(default=False, verbose_name="Tavsiya etilgan")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    
    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200, verbose_name="Kompaniya")
    position = models.CharField(max_length=200, verbose_name="Lavozim")
    description = models.TextField(verbose_name="Tavsif")
    start_date = models.DateField(verbose_name="Boshlash sanasi")
    end_date = models.DateField(null=True, blank=True, verbose_name="Tugash sanasi")
    current = models.BooleanField(default=False, verbose_name="Hozirgi ish")
    order = models.IntegerField(default=0, verbose_name="Tartib")
    
    class Meta:
        verbose_name = "Ish tajribasi"
        verbose_name_plural = "Ish tajribalari"
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=200, verbose_name="O'quv yurti")
    degree = models.CharField(max_length=200, verbose_name="Daraja")
    field_of_study = models.CharField(max_length=200, verbose_name="O'qish yo'nalishi")
    start_date = models.DateField(verbose_name="Boshlash sanasi")
    end_date = models.DateField(null=True, blank=True, verbose_name="Tugash sanasi")
    current = models.BooleanField(default=False, verbose_name="Hozirgi o'qish")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    
    class Meta:
        verbose_name = "Ta'lim"
        verbose_name_plural = "Ta'lim"
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.degree} in {self.field_of_study}"

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Mavzu")
    message = models.TextField(verbose_name="Xabar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    read = models.BooleanField(default=False, verbose_name="O'qilgan")
    
    class Meta:
        verbose_name = "Aloqa"
        verbose_name_plural = "Aloqa"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class ChatMessage(models.Model):
    username = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}: {self.message[:20]}"

class SocialLink(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='social_links', verbose_name="Shaxsiy ma'lumot")
    name = models.CharField(max_length=30, verbose_name="Tarmoq nomi")
    icon = models.CharField(max_length=50, verbose_name="Ikon sinfi (masalan, 'fab fa-telegram')")
    url = models.URLField(verbose_name="Havola")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Ijtimoiy tarmoq"
        verbose_name_plural = "Ijtimoiy tarmoqlar"
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.url})"

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name="Loyiha")
    image = models.ImageField(upload_to='projects/', verbose_name="Rasm")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Loyiha rasmi"
        verbose_name_plural = "Loyihalar rasmlari"
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - {self.image.name}"

class Certificate(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nomi")
    description = models.TextField(verbose_name="Tavsif")
    image = models.ImageField(upload_to='certificates/', verbose_name="Sertifikat rasmi")
    date = models.DateField(verbose_name="Olingan sana")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"
        ordering = ['-date', 'order']

    def __str__(self):
        return self.title
