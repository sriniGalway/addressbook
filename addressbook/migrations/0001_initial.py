# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 00:51
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be Alphanumeric"', regex='^[a-zA-Z0-9]*$')])),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntryModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('mobile', models.CharField(error_messages={'blank': 'This field is cannot be empty, please try again.', 'unique': 'This Mobile Number is not unique, please try again.'}, help_text='Must be a unique Mobile Number.', max_length=30, unique=True, verbose_name='Mobile Number')),
                ('address', models.CharField(max_length=80)),
                ('email', models.EmailField(error_messages={'blank': 'This field is cannot be empty, please try again.', 'unique': 'This e-mail address is not unique, please try again.'}, help_text='Must be a unique e-mail address.', max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
