from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.

from django.db import models

class Coli(models.Model):
    client = models.CharField(max_length= 30)
    numeros_colis = models.CharField(max_length=30)
    
    def __str__(self):
        return self.numeros_colis
    


class Position(models.Model):
    
    location = PlainLocationField(zoom=7)
    date = models.DateField(auto_now_add=True)
    heure = models.TimeField(auto_now_add=True)
    coli = models.ForeignKey(Coli, on_delete=models.SET_NULL,null=True, related_name="coli")
    
    def __str__(self):
        return self.coli.numeros_colis
    
