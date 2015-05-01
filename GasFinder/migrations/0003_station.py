# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GasFinder', '0002_auto_20150410_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('address', models.CharField(max_length=150, serialize=False, primary_key=True)),
                ('octane87', models.DecimalField(max_digits=3, decimal_places=2)),
                ('octane89', models.DecimalField(max_digits=3, decimal_places=2)),
                ('octane92', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
