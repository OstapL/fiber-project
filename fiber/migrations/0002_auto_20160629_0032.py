# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 00:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('fiber', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='page',
            managers=[
                ('tree', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(max_length=255, upload_to='uploads/files', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(max_length=255, upload_to='uploads/images', verbose_name='image'),
        ),
    ]