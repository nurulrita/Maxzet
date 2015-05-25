# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxzet', '0002_auto_20150506_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='kategori',
            field=models.CharField(max_length=1, choices=[(b'D', b'Dress'), (b'A', b'Atasan'), (b'B', b'Bawahan'), (b'O', b'Outerwear')]),
            preserve_default=True,
        ),
    ]
