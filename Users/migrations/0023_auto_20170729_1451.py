# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-29 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0022_auto_20170729_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='school_studied',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='school_studied',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
