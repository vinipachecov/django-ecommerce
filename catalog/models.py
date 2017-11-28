# coding=utf-8

from django.db import models
from django.core.urlresolvers import reverse


    


class Category(models.Model):

    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('ID', max_length=100)

    created = models.DateTimeField('Created in', auto_now_add=True)
    modified = models.DateTimeField('Modified in', auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})


class Product(models.Model):

    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('ID', max_length=100)
    category = models.ForeignKey('catalog.Category', verbose_name='Category')
    description = models.TextField('Description', blank=True)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    created = models.DateTimeField('Created in ', auto_now_add=True)
    modified = models.DateTimeField('Modified in', auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})
