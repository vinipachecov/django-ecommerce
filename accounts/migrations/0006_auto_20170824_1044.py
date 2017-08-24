# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-24 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170824_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Equipe'),
        ),
    ]
