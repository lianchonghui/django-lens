# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-24 09:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='description')),
                ('full', models.ImageField(upload_to='lens/%Y/%m/%d/', verbose_name='full')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
