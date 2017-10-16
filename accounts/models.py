# coding=utf-8

import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Nick / User', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Use a valid username. '
                'It must have only letters, numbers'
                'and the characters: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='A nickname will be used to identify you in the platform'
    )
    name = models.CharField('Name', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Staff', default=False)
    is_active = models.BooleanField('Active', default=True)
    date_joined = models.DateTimeField('Joined in', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
