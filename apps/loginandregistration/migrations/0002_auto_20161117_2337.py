# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 23:37
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('loginandregistration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('Usermgr', django.db.models.manager.Manager()),
            ],
        ),
    ]
