# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20170214_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Sex',
            field=models.CharField(max_length=2),
        ),
    ]