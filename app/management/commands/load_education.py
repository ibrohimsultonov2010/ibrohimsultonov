from django.core.management.base import BaseCommand
from app.models import Education
from datetime import date

class Command(BaseCommand):
    help = 'Load education information'

    def handle(self, *args, **options):
        # Clear existing education
        Education.objects.all().delete()
        
        # Education data
        education_data = [
            {
                'institution': 'Toshkent Axborot Texnologiyalari Universiteti',
                'degree': 'Bakalavr',
                'field_of_study': 'Dasturiy ta\'minot muhandisligi',
                'start_date': date(2019, 9, 1),
                'end_date': date(2023, 6, 30),
                'current': False,
                'description': 'Web texnologiyalari, ma\'lumotlar bazasi va dasturlash asoslari bo\'yicha ta\'lim olgan.'
            },
            {
                'institution': 'Udemy Online Platform',
                'degree': 'Sertifikat',
                'field_of_study': 'Django Web Development',
                'start_date': date(2022, 1, 1),
                'end_date': date(2022, 3, 31),
                'current': False,
                'description': 'Django framework, REST API va zamonaviy web texnologiyalari bo\'yicha kurs.'
            }
        ]
        
        # Create education
        for edu_data in education_data:
            education = Education.objects.create(**edu_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created education: {education.degree} in {education.field_of_study} at {education.institution}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(education_data)} education records!')
        ) 