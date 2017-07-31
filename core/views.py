# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from catalog.models import Category
from .forms import ContactForm


def index(request):
    context = {
        'categories' : Category.objects.all()
    }
    return render(request, 'index.html', context)


def contact(request):
    success = False
    form  = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()            
        success = True
    context = {
        'form' : form,
        'success' : success
    }
    return render(request, 'contact.html', context)


def product_list(request):
    return render(request, 'product_list.html')
