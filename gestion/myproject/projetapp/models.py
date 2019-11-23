from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
    
'''
# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # 1 user <---> 1 profil

    fonction = models.CharField(max_length=50, null=True)
    contacts = models.CharField(max_length=30, null=True)
    addresse = models.CharField(max_length=30, null=True)
    promotion = models.CharField(max_length=30, null=True)
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

class Commit(models.Moodel):
    id_commit = models.CharField(max_length=200)
    user = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='commit_user')
    projet = models.ForeignKey('Projet', on_delete = models.CASCADE, related_name='commit_user')
    comment = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True )
    page_modif = models.TextField()
    status = models.BooleanField( default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)

class Tache(models.Model):
    nom = models.CharField(max_length=50)
    status = models.BooleanField( default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = " Tache"
        verbose_name_plural = "Taches"

    def __str__(self):
        return self.nom

class Projet(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    charge = models.FileField()
    image = models.ImageField(upload_to="images")
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    duree = models.DurationField()
    participant = models.ManyToManyField(Profile)
    taches = models.ManyToManyField(Tache)
    nombre_commit = models.IntegerField()
    etat_actuel = models.PositiveIntegerField(default = 0)
    status = models.BooleanField( default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = " Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.nom
    
class Tchat(models.Model):
    user = models.ForeignKey(Profile)
    message = models.CharField(max_length= 500)
    status = models.BooleanField( default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    
        
'''
