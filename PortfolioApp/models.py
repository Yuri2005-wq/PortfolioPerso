from django.utils import timezone

from django.db import models

class Portfolio(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.PositiveIntegerField(max_length=20)
    ville = models.CharField(max_length=100)
    diplome = models.CharField(max_length=100)
    email = models.EmailField()
    disponibilite = models.CharField(max_length=100)
    profile = models.FileField(upload_to='photo/', null=True, blank=True)
    def __str__(self):
        return self.nom

class Projet(models.Model):
    image = models.ImageField(upload_to='project', null=True, blank=True)
    libelle = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    language = models.CharField(max_length=100, default='Python')
    base_donnee = models.CharField(max_length=100, default="Mysql")
    en_pluse = models.CharField(max_length=100, default="API")
    balise = models.CharField(max_length=100, default="HTML")
    style = models.CharField(max_length=100, default="CSS")
    script = models.CharField(max_length=100, default="JavaScript")
    def __str__(self):
        return self.libelle

class ContactMoi (models.Model):
    Full_name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.PositiveIntegerField(default=0)
    sujet = models.CharField(max_length=100)
    messages = models.TextField()
    date_publication = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.Full_name}-{self.sujet} - {self.messages}'



