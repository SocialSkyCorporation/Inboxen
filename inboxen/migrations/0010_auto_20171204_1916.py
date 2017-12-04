# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-04 19:16
from __future__ import unicode_literals

from django.db import migrations
from salmon.encoding import normalize_header


def fix_headers(apps, schema_editor):
    HeaderName = apps.get_model("inboxen", "HeaderName")
    Header = apps.get_model("inboxen", "Header")

    # find header names that have not been normalized
    for name in HeaderName.objects.all():
        normalized_name = normalize_header(name.name)
        if normalized_name != name.name:
            # get or create normalized header name
            new_name, _ = HeaderName.objects.get_or_create(name=normalized_name)
            # update headers with not normalized headers with normalized ones
            Header.objects.filter(name=name).update(name=new_name)


class Migration(migrations.Migration):

    dependencies = [
        ('inboxen', '0009_auto_20170518_1946'),
    ]

    operations = [
        migrations.RunPython(fix_headers, reverse_code=lambda x, y: None),
    ]
