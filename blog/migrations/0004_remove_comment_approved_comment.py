# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-03 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_approved_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
