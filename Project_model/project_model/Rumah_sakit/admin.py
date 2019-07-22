from django.contrib import admin

# Register your models here.

from .models import Dokter, Pasien, Resep, Obat      


class DokterAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon', 'bidang']  
    list_display_links = ['nama']
    list_filter = ['bidang']
    
class PasienAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon', 'keluhan']  
    list_display_links = ['nama']

class ResepAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'total_harga', 'kumpulan_obat']  
    list_display_links = ['nama']
    list_filter = ['nama']

class ObatAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'kandungan']  
    list_display_links = ['nama']
    list_filter = ['nama']

admin.site.register(Dokter, DokterAdmin)
admin.site.register(Pasien, PasienAdmin)
admin.site.register(Resep, ResepAdmin)
admin.site.register(Obat, ObatAdmin)
