from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, name, login, password, is_superuser=False):
        if login is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('Users must have a password.')

        user = self.model(login=login, name=name, is_superuser=is_superuser)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField('user id', primary_key=True, editable=False)
    email = models.EmailField('user email', max_length=20, unique=True)
    name = models.CharField('user name', max_length=100)
    password = models.CharField('user password', max_length=500)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    objects = UserManager()

    def __str__(self):
        return f'{str(self.id)}'

    class Meta:
        db_table = 'users'