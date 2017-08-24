# coding=utf-8


from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


    # tem uma classe meta onde eu indico um modelo
    #  e os campos
    #  a senha não vai ser colocada de forma direta
class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']
