# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legco', '0006_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(max_length=512),
        ),
    ]
