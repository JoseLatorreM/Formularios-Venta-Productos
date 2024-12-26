from django.contrib import admin
from AplicacionRecu.models import Tiquet

class TiquetAdmin(admin.ModelAdmin):
    list_display = ['id','Nom_C','Nom_Eje','Descripcion','TipoT','Criticidad','Estado',]

admin.site.register(Tiquet, TiquetAdmin)