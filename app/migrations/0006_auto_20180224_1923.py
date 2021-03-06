# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-24 19:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180224_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='voters',
            field=models.ManyToManyField(related_name='upvoted_items', to=settings.AUTH_USER_MODEL),
        ),
    ]
