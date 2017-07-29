# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-28 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_auto_20170728_0520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='alumni',
            name='bio',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='dept_alum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Level'),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='phone_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='work_field_main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Interest'),
        ),
        migrations.AlterField(
            model_name='student',
            name='bio',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='student',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='dept_stud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Level'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='username_roll',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='work_field_main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Interest'),
        ),
        migrations.DeleteModel(
            name='course_in',
        ),
        migrations.DeleteModel(
            name='departments',
        ),
        migrations.DeleteModel(
            name='interests',
        ),
    ]