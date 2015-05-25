# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maxzet', '0006_auto_20150512_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransaksiWomen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alamat_pengiriman', models.TextField()),
                ('jenis_pembayaran', models.CharField(max_length=17, choices=[(b'Transfer', b'Transfer'), (b'COD', b'Cash on Delivery')])),
                ('total_bayar', models.IntegerField()),
                ('barang', models.ForeignKey(related_name='transaksi-women', to='maxzet.Women')),
                ('pembeli', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='men',
            name='harga',
            field=models.DecimalField(max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
