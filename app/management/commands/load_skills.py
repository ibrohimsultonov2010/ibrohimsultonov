from django.core.management.base import BaseCommand
from app.models import Skill

class Command(BaseCommand):
    help = 'Load skills from txt file'

    def handle(self, *args, **options):
        # Clear existing skills
        Skill.objects.all().delete()
        
        # Skills data
        skills_data = [
            ('Python', 'programming', 90, 'fab fa-python', 1),
            ('JavaScript', 'programming', 50, 'fab fa-js-square', 2),
            ('CSS', 'framework', 100, 'fab fa-css3-alt', 3),
            ('HTML', 'framework', 100, 'fab fa-html5', 4),
            ('Bootstrap', 'framework', 100, 'fab fa-bootstrap', 5),
        ]
        
        # Create skills
        for name, category, proficiency, icon, order in skills_data:
            skill = Skill.objects.create(
                name=name,
                category=category,
                proficiency=proficiency,
                icon=icon,
                order=order
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created skill: {skill.name} ({skill.proficiency}%)')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(skills_data)} skills!')
        ) 