from django.core.management.base import BaseCommand
from app.models import Project

class Command(BaseCommand):
    help = 'Load sample projects'

    def handle(self, *args, **options):
        # Clear existing projects
        Project.objects.all().delete()
        
        # Projects data
        projects_data = [
            {
                'title': 'Portfolio Website',
                'description': 'Zamonaviy va responsive portfolio sayti. Django, Bootstrap va JavaScript ishlatilgan. Chiroyli animatsiyalar va interaktiv elementlar bilan.',
                'technologies': 'Django, Python, HTML, CSS, JavaScript, Bootstrap',
                'github_url': 'https://github.com/ibrohim301/portfolio',
                'live_url': 'https://ibrohim-portfolio.com',
                'featured': True
            },
            {
                'title': 'E-commerce Platform',
                'description': 'To\'liq funksional online do\'kon. Mahsulotlar katalogi, savat, to\'lov tizimi va admin panel mavjud.',
                'technologies': 'Django, Python, PostgreSQL, HTML, CSS, JavaScript',
                'github_url': 'https://github.com/ibrohim301/ecommerce',
                'live_url': 'https://shop.example.com',
                'featured': True
            },
            {
                'title': 'Task Management App',
                'description': 'Vazifalarni boshqarish ilovasi. Foydalanuvchilar vazifalar yaratish, tahrirlash va o\'chirish mumkin.',
                'technologies': 'Django, Python, SQLite, HTML, CSS, JavaScript',
                'github_url': 'https://github.com/ibrohim301/task-manager',
                'live_url': '',
                'featured': False
            }
        ]
        
        # Create projects
        for project_data in projects_data:
            project = Project.objects.create(**project_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created project: {project.title}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(projects_data)} projects!')
        ) 