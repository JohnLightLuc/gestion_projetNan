from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
    
'''   
# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # 1 user <---> 1 profil


    contacts = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='profile/', default='useravatar.png')
    birth_date = models.DateField(null=True)

    # Initialisation a la creation

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):

        instance.profile.save()


class Projet(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    charge = models.FileField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    participant = models.ManyToManyField(User)
    nombre_commit = models.IntegerField()
    status = models.BooleanField( default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = " Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.nom
        
'''
