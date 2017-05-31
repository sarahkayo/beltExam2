# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0002_auto_20170531_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('wish_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belt_app.Item')),
                ('wish_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belt_app.User')),
            ],
        ),
    ]
