# coding=utf-8

from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):

    name = forms.CharField(label ='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())


    # def __init__(self,*args,**kwargs):
    #     super(ContactForm, self).__init__(*args,**kwargs)
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['message'].widget.attrs['class'] = 'form-control'


    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome: {0}\nEmail:{1}\n{2}'.format(name, email, message)
        send_mail(
            'Contato do Django E-commerce',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]
        )
