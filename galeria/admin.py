from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "categoria", "foto", "publicada")
    list_display_links = ("id", "nome", "legenda")
    search_fields = ("id", "nome")
    list_filter = ("categoria", "publicada")
    list_editable = ("categoria", "publicada",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)