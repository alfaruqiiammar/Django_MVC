from django.db import models

# Create your models here.

class Direksi(models.Model):
    nama_lengkap = models.TextField(max_length=100)
    nomor_telepon = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=50)





class Mentee(models.Model):
    nama_lengkap = models.TextField(max_length=100)
    nomor_telepon = models.CharField(max_length=50)
    nomor_absen = models.CharField(max_length=10)
    nilai_rata_rata = models.CharField(max_length=20)



class Mata_pelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=50)
    jadwal_dimulai = models.DateField()
    jadwal_berakhir = models.DateField()
    def __str__(self):
        return self.nama_pelajaran




class Mentor(models.Model):
    nama_lengkap = models.TextField(max_length=100)
    nomor_telepon = models.CharField(max_length=50)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)
    




class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=50)
    banyak_soal = models.CharField(max_length=50)
    bobot_nilai = models.CharField(max_length=50)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)




class Live_code(models.Model):
    nama_live_code = models.CharField(max_length=50)
    banyak_soal = models.CharField(max_length=50)
    bobot_nilai = models.CharField(max_length=50)
    tanggal_pelaksanaan = models.DateField()
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)
