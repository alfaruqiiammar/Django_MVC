# Generated by Django 2.2.3 on 2019-07-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rumah_sakit', '0002_auto_20190722_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokter',
            name='nomor_telepon',
            field=models.CharField(max_length=20),
        ),
    ]