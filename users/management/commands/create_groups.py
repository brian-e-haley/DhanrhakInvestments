from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

GROUPS = {'student', 'teacher'}
APPS = {'profiles'}
PERMISSIONS = {'add', 'change', 'delete', 'view'}
MODELS = {'Quiz', 'Question', 'Option'}


class Command(BaseCommand):
    help = 'Creates teacher and student groups.'

    def handle(self, *args, **options):
        self.stdout.write('Creating the student and teacher group.')
        Group.objects.get_or_create(name='student')
        Group.objects.get_or_create(name='teacher')
        self.stdout.write('Student and teacher groups created successfully.')
