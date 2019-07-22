from django.contrib import admin

# Register your models here.

from .models import Hewan, Kandang, Penjaga, Pengunjung

class HewanAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'species']  
    list_display_links = ['nama']
    list_filter = ['species']

class KandangAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'isi_kandang', 'luas_kandang']  
    list_display_links = ['nama']

class PenjagaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon', 'jadwal_jaga']  
    list_display_links = ['nama']
    list_filter = ['jadwal_jaga']

class PengunjungAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon', 'hari_berkunjung']  
    list_display_links = ['nama']
    list_filter = ['hari_berkunjung']

admin.site.register(Hewan, HewanAdmin)
admin.site.register(Kandang, KandangAdmin)
admin.site.register(Penjaga, PenjagaAdmin)
admin.site.register(Pengunjung, PengunjungAdmin)
