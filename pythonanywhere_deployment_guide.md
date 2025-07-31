# PythonAnywhere ga Portfolio Loyihasini Deploy Qilish Qo'llanmasi

## 1. PythonAnywhere da hisob yarating
- https://www.pythonanywhere.com ga kiring
- Bepul hisob yarating

## 2. Konsol oching
- Dashboard da "Consoles" bo'limiga o'ting
- "Bash" konsolini oching

## 3. Loyihani yuklang
```bash
# Loyiha papkasiga o'ting
cd ~

# Git dan loyihani klonlang (agar GitHub da bo'lsa)
git clone https://github.com/yourusername/portfolll.git

# Yoki loyihani yuklang
# (Loyiha fayllarini PythonAnywhere ga yuklang)
```

## 4. Virtual environment yarating
```bash
# Virtual environment yarating
python3 -m venv portfolio_env

# Virtual environment ni faollashtiring
source portfolio_env/bin/activate

# Pip ni yangilang
pip install --upgrade pip
```

## 5. Kerakli kutubxonalarni yuklang
```bash
# Minimal kutubxonalarni yuklang
pip install -r requirements_minimal.txt

# Yoki alohida yuklang:
pip install Django==5.2.2
pip install Pillow==11.2.1
pip install django-crispy-forms==2.4
pip install crispy-bootstrap5==2025.6
```

## 6. Django sozlamalarini yangilang
```bash
# Loyiha papkasiga o'ting
cd portfolll

# Ma'lumotlar bazasini yarating
python manage.py makemigrations
python manage.py migrate

# Superuser yarating
python manage.py createsuperuser

# Static fayllarni yig'ing
python manage.py collectstatic --noinput
```

## 7. Web app yarating
- Dashboard da "Web" bo'limiga o'ting
- "Add a new web app" ni bosing
- "Manual configuration" ni tanlang
- Python versiyasini tanlang (3.9 yoki undan yuqori)

## 8. WSGI faylini sozlang
- Web app da "WSGI configuration file" ni oching
- Quyidagi kodni qo'shing:

```python
import os
import sys

# Loyiha yo'lini qo'shing
path = '/home/yourusername/portfolll'
if path not in sys.path:
    sys.path.append(path)

# Django sozlamalarini o'rnating
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

# Django application ni import qiling
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 9. Settings.py ni yangilang
```python
# project/settings.py faylida:

# DEBUG ni False qiling
DEBUG = False

# ALLOWED_HOSTS ga domain qo'shing
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# Static files sozlamalari
STATIC_URL = '/static/'
STATIC_ROOT = '/home/yourusername/portfolll/staticfiles'

# Media files sozlamalari
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/yourusername/portfolll/media'
```

## 10. Static files yo'lini sozlang
- Web app da "Static files" bo'limiga o'ting
- Quyidagilarni qo'shing:
  - URL: `/static/`
  - Directory: `/home/yourusername/portfolll/staticfiles`

## 11. Ma'lumotlarni yuklang
```bash
# Konsol da:
cd ~/portfolll
source portfolio_env/bin/activate

# Ma'lumotlarni yuklang
python manage.py load_all_data
```

## 12. Web app ni qayta ishga tushiring
- Web app da "Reload" tugmasini bosing

## 13. Loyihani tekshiring
- https://yourusername.pythonanywhere.com ga kiring
- Loyiha ishlayotganini tekshiring

## Xatoliklar va yechimlar:

### 1. Import xatosi
```bash
# Virtual environment ni faollashtiring
source portfolio_env/bin/activate
```

### 2. Static files topilmaydi
```bash
# Static fayllarni qayta yig'ing
python manage.py collectstatic --noinput
```

### 3. Ma'lumotlar bazasi xatosi
```bash
# Migratsiyalarni qayta ishga tushiring
python manage.py migrate
```

### 4. Permission xatosi
```bash
# Fayl huquqlarini tekshiring
chmod 755 ~/portfolll
chmod 644 ~/portfolll/*.py
```

## Foydali buyruqlar:
```bash
# Loyiha holatini tekshirish
python manage.py check

# Ma'lumotlar bazasini tekshirish
python manage.py dbshell

# Django shell
python manage.py shell

# Log fayllarini ko'rish
tail -f ~/portfolll/logs/django.log
```

## Eslatmalar:
- PythonAnywhere bepul hisobda kuniga 512MB RAM
- Loyiha 24/7 ishlaydi
- Har 3 oyda qayta ishga tushirish kerak
- Backup qilishni unutmang

## Xavfsizlik:
- DEBUG = False
- SECRET_KEY ni o'zgartiring
- Admin panel parolini kuchli qiling
- HTTPS ishlatishni tavsiya etamiz 