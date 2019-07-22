# Generated by Django 2.2.3 on 2019-07-22 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hewan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=50)),
                ('species', models.CharField(max_length=50)),
                ('berat', models.CharField(max_length=20)),
                ('umur', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kandang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('isi_kandang', models.CharField(max_length=50)),
                ('luas_kandang', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=100)),
                ('nomor_telepon', models.CharField(max_length=20)),
                ('hari_berkunjung', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Penjaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=100)),
                ('nomor_telepon', models.CharField(max_length=20)),
                ('jadwal_jaga', models.CharField(max_length=100)),
            ],
        ),
    ]
