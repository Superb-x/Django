# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='Sex',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='students',
            name='Telephone',
            field=models.CharField(default=18932463349, max_length=20),
            preserve_default=False,
        ),
    ]