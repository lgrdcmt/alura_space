from django.contrib import admin
from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "categoria", "publicada",)
    list_display_links = ("id", "nome", "legenda",)
    search_fields = ("id", "nome",)
    list_filter = ("categoria", "publicada", "usuario",)
    list_editable = ("categoria", "publicada",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)