# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='tweeted',
            field=models.BooleanField(default=False),
        ),
    ]
