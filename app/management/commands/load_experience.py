from django.core.management.base import BaseCommand
from app.models import Experience
from datetime import date

class Command(BaseCommand):
    help = 'Load work experience'

    def handle(self, *args, **options):
        # Clear existing experience
        Experience.objects.all().delete()
        
        # Experience data
        experience_data = [
            {
                'company': 'Tech Solutions LLC',
                'position': 'Senior Full Stack Developer',
                'description': 'Zamonaviy web ilovalar yaratish, jamoani boshqarish va texnik arxitektura ustida ishlash. Django, React va PostgreSQL texnologiyalarini ishlatish.',
                'start_date': date(2023, 1, 1),
                'end_date': None,
                'current': True,
                'order': 1
            },
            {
                'company': 'Digital Innovations',
                'position': 'Python Developer',
                'description': 'Backend ilovalar yaratish, API dizayn va ma\'lumotlar bazasi optimizatsiyasi. Django REST framework va PostgreSQL bilan ishlash.',
                'start_date': date(2022, 3, 1),
                'end_date': date(2022, 12, 31),
                'current': False,
                'order': 2
            },
            {
                'company': 'StartUp Studio',
                'position': 'Junior Developer',
                'description': 'Web saytlar yaratish, frontend va backend ishlab chiqish. HTML, CSS, JavaScript va Python texnologiyalarini o\'rganish.',
                'start_date': date(2021, 6, 1),
                'end_date': date(2022, 2, 28),
                'current': False,
                'order': 3
            }
        ]
        
        # Create experience
        for exp_data in experience_data:
            experience = Experience.objects.create(**exp_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created experience: {experience.position} at {experience.company}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(experience_data)} experience records!')
        ) 