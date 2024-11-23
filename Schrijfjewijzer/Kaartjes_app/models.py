from django.db import models

# Create your models here.
class kind_Schoolvakken(models.Model):
    naam = models.CharField(max_length=50)
    Rekenen = models.CharField(max_length=50)
    Taal = models.CharField(max_length=50)
    Spelling = models.CharField(max_length=50)
    Technisch_lezen = models.CharField(max_length=50)
    Overig = models.CharField(max_length=75)
    
    class Meta:
        verbose_name_plural = "Kinderen en vakken"

    def __str__(self):
        return self.naam