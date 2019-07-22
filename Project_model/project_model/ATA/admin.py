from django.contrib import admin

# Register your models here.

from .models import Direksi, Mentee, Mentor, Mata_pelajaran, Challenge, Live_code      


class DireksiAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama_lengkap', 'nomor_telepon', 'jabatan']  
    list_display_links = ['nama_lengkap']
    list_filter = ['jabatan']


class MenteeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama_lengkap', 'nomor_telepon', 'nilai_rata_rata']  
    list_display_links = ['nama_lengkap']

class Mata_pelajaranAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama_pelajaran', 'jadwal_dimulai', 'jadwal_berakhir']  
    list_display_links = ['nama_pelajaran']
    list_filter = ['jadwal_dimulai', 'jadwal_berakhir']

class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama_lengkap', 'nomor_telepon', 'mata_pelajaran']  
    list_display_links = ['nama_lengkap']
    list_filter = ['mata_pelajaran']
   

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama_challenge', 'mata_pelajaran']  
    list_display_links = ['nama_challenge']

class Live_codeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama_live_code', 'tanggal_pelaksanaan', 'mata_pelajaran']  
    list_display_links = ['nama_live_code']
  

admin.site.register(Direksi, DireksiAdmin)
admin.site.register(Mentee, MenteeAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Mata_pelajaran, Mata_pelajaranAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Live_code, Live_codeAdmin)
