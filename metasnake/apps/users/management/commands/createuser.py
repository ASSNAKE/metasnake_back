from django.core.management.base import BaseCommand
from metasnake.apps.users.models import User
from django.conf import settings
from django.contrib.auth.hashers import make_password


SECRET_KEY = settings.SECRET_KEY


class Command(BaseCommand):
    help = 'Create user | python manage.py createuser "email" "password"'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('password', type=str, help='User password')

    def handle(self, *args, **kwargs):
        try:
            email = kwargs['email']
            name = kwargs['name']
            password = kwargs['password']
            encrypted_password = make_password(password, SECRET_KEY)
            user = User(email=email,
                        name=name,
                        password=encrypted_password)
            user.save()
            self.stdout.write(f'Пользователь создан.')
        except Exception as e:
            self.stdout.write(f'Произошла ошибка | {str(e)}')