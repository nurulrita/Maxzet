# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxzet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='kategori',
            field=models.CharField(default='', max_length=1, choices=[(b'M', b'Men'), (b'W', b'Women')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='barang',
            name='kode_barang',
            field=models.CharField(default='', max_length=14),
            preserve_default=False,
        ),
    ]
