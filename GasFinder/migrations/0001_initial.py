# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('tiers', models.CharField(default=b'Bronze', max_length=1000, choices=[(b'Bronze', b'Bronze Tier: $1000 per month'), (b'Silver', b'Silver Tier: $3000 per month'), (b'Gold', b'Gold Tier: $5000 per month'), (b'Platinum', b'Platinum Tier: $7000 per month')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
