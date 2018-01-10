# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-31 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import inboxen.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inboxen', '0010_auto_20171204_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body',
            name='hashed',
            field=models.CharField(max_length=80, unique=True, validators=[inboxen.validators.ProhibitNullCharactersValidator()]),
        ),
        migrations.AlterField(
            model_name='domain',
            name='domain',
            field=models.CharField(max_length=253, unique=True, validators=[inboxen.validators.ProhibitNullCharactersValidator()]),
        ),
        migrations.AlterField(
            model_name='headerdata',
            name='data',
            field=models.TextField(validators=[inboxen.validators.ProhibitNullCharactersValidator()]),
        ),
        migrations.AlterField(
            model_name='headerdata',
            name='hashed',
            field=models.CharField(max_length=80, unique=True, validators=[inboxen.validators.ProhibitNullCharactersValidator()]),
        ),
        migrations.AlterField(
            model_name='headername',
            name='name',
            field=models.CharField(max_length=78, unique=True, validators=[inboxen.validators.ProhibitNullCharactersValidator()]),
        ),
        migrations.AlterField(
            model_name='inbox',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True, validators=[inboxen.validators.ProhibitNullCharactersValidator()]),
        ),
        migrations.AlterField(
            model_name='inbox',
            name='inbox',
            field=models.CharField(max_length=64, validators=[inboxen.validators.ProhibitNullCharactersValidator()]),
        ),
        migrations.AlterField(
            model_name='liberation',
            name='_path',
            field=models.CharField(max_length=255, null=True, unique=True, validators=[inboxen.validators.ProhibitNullCharactersValidator()]),
        ),
        migrations.AlterField(
            model_name='request',
            name='result',
            field=models.CharField(blank=True, max_length=1024, null=True, validators=[inboxen.validators.ProhibitNullCharactersValidator()], verbose_name=b'comment'),
        ),
    ]