from django.db import models

# Create your models here.


class Dokter(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=20)
    bidang = models.CharField(max_length=255)
    jadwal_praktek = models.DateField()


class Pasien(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=50)
    alamat = models.TextField(max_length=100)
    keluhan = models.TextField(max_length=100)


class Resep(models.Model):
    nama = models.CharField(max_length=255)
    total_harga = models.CharField(max_length=50)
    kumpulan_obat = models.CharField(max_length=100)

class Obat(models.Model):
    nama = models.CharField(max_length=255)
    kandungan = models.TextField(max_length=200)
    khasiat = models.TextField(max_length=200)