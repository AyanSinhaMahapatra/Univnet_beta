# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_auto_20170728_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='cv_url',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='cv_url',
            field=models.CharField(max_length=300),
        ),
    ]
