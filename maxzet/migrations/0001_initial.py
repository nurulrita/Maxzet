# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_lengkap', models.CharField(max_length=30)),
                ('jenis_kelamin', models.CharField(max_length=1, choices=[(b'L', b'Laki-Laki'), (b'P', b'Perempuan')])),
                ('tanggal_lahir', models.DateField()),
                ('no_hp', models.CharField(max_length=12)),
                ('alamat', models.CharField(max_length=50)),
                ('kode_pos', models.CharField(max_length=5)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
