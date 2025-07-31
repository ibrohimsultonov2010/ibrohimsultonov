from django.core.management.base import BaseCommand
from app.models import PersonalInfo

class Command(BaseCommand):
    help = 'Load personal information'

    def handle(self, *args, **options):
        # Clear existing personal info
        PersonalInfo.objects.all().delete()
        
        # Create personal info
        personal_info = PersonalInfo.objects.create(
            name='Ibrohim Sultonov',
            title='Full Stack Developer',
            description='Zamonaviy web texnologiyalari bilan ishlaydigan tajribali dasturchi. Chiroyli va funksional web saytlar yaratishda mutaxassis. Python, Django, JavaScript va zamonaviy frontend texnologiyalari bilan ishlashda tajribaga ega.',
            email='ibrohim.sultonov@example.com',
            phone='+998 90 123 45 67',
            location='Toshkent, O\'zbekiston',
            github='https://github.com/ibrohim301',
            linkedin='https://linkedin.com/in/ibrohim-sultonov',
            twitter='https://twitter.com/ibrohim301'
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created personal info for: {personal_info.name}')
        ) 