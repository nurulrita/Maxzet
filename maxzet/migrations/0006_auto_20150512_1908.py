# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxzet', '0005_transaksimen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='men',
            name='harga',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
