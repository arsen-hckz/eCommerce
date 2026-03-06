from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(email='admin@admin.com').exists():
            u = User.objects.create_superuser(
                email='admin@admin.com',
                username='admin',
                password='admin123'
            )
            u.is_staff = True
            u.is_admin = True
            u.save()
            self.stdout.write('Superuser created')
        else:
            self.stdout.write('Superuser already exists')