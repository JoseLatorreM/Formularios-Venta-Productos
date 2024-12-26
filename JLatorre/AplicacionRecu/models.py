from django.db import models
# Create your models here.
class Tiquet(models.Model):
    Nom_C = models.CharField (max_length=30 ,)
    Nom_Eje = models.CharField(max_length=20,)
    Descripcion = models.DecimalField(max_length=30,)
    TipoT = models.CharField(max_length=30,)
    Criticidad = models.DecimalField(max_length=30,)
    Estado = models.DecimalField(max_length=30)