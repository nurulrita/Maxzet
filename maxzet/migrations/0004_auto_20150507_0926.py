# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxzet', '0003_auto_20150507_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Men',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kategori', models.CharField(max_length=1, choices=[(b'A', b'Atasan'), (b'K', b'Kemeja'), (b'B', b'Bawahan'), (b'O', b'Outerwear')])),
                ('kode_barang', models.CharField(max_length=14)),
                ('nama', models.CharField(max_length=50)),
                ('merk', models.CharField(max_length=30)),
                ('harga', models.DecimalField(max_digits=10, decimal_places=2)),
                ('gambar', models.URLField()),
                ('deskripsi', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kategori', models.CharField(max_length=1, choices=[(b'D', b'Dress'), (b'A', b'Atasan'), (b'B', b'Bawahan'), (b'O', b'Outerwear')])),
                ('kode_barang', models.CharField(max_length=14)),
                ('nama', models.CharField(max_length=50)),
                ('merk', models.CharField(max_length=30)),
                ('harga', models.DecimalField(max_digits=10, decimal_places=2)),
                ('gambar', models.URLField()),
                ('deskripsi', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Barang',
        ),
    ]
