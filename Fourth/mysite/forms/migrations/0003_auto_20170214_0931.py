# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 01:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20170214_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='Telephone',
            new_name='Tel',
        ),
    ]
