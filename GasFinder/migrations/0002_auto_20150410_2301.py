# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GasFinder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertiser',
            old_name='company_name',
            new_name='name',
        ),
    ]
