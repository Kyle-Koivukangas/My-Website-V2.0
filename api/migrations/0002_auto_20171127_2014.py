# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 04:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 27, 20, 14, 14, 108242)),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]
