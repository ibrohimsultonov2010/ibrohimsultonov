from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Load all data (skills, personal info, projects, experience, education)'

    def handle(self, *args, **options):
        self.stdout.write('Loading all data...')
        
        # Load all data
        call_command('load_skills')
        call_command('load_personal_info')
        call_command('load_projects')
        call_command('load_experience')
        call_command('load_education')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully loaded all data!')
        ) 