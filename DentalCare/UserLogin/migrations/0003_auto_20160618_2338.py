# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-18 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserLogin', '0002_auto_20160616_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]