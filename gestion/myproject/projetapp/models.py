from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)