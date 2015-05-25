# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maxzet', '0004_auto_20150507_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransaksiMen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alamat_pengiriman', models.TextField()),
                ('jenis_pembayaran', models.CharField(max_length=17, choices=[(b'Transfer', b'Transfer'), (b'COD', b'Cash on Delivery')])),
                ('total_bayar', models.IntegerField()),
                ('barang', models.ForeignKey(related_name='transaksi-men', to='maxzet.Men')),
                ('pembeli', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
