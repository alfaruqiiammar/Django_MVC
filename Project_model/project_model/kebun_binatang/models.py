from django.db import models

# Create your models here.

class Hewan(models.Model):
    nama = models.TextField(max_length=50)
    species = models.CharField(max_length=50)
    berat = models.CharField(max_length=20)
    umur = models.CharField(max_length=10)



class Kandang(models.Model):
    nama = models.CharField(max_length=100)
    isi_kandang = models.CharField(max_length=50)
    luas_kandang = models.CharField(max_length=50)





class Penjaga(models.Model):
    nama = models.TextField(max_length=100)
    nomor_telepon = models.CharField(max_length=20)
    jadwal_jaga = models.CharField(max_length=100)





class Pengunjung(models.Model):
    nama = models.TextField(max_length=100)
    nomor_telepon = models.CharField(max_length=20)
    hari_berkunjung = models.CharField(max_length=100)
