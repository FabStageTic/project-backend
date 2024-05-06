from django.db import models
from autheur.models import Autheur
# Create your models here.

choices = [('L','L'), ('ml','ml'), ('kg','kg'), ('g','g') ,('CaC', 'CaC'), ('CaS','CaS')]

class Ingredient(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    alternatives = models.ManyToManyField('self', symmetrical=False, related_name='alternative_to', blank=True)
    
    def __str__(self):
        return f'{self.nom}'
    
#class Variete(models.Model):
#    ingredient_original = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True, blank=True, related_name='ingredient')
#    ingredient_alternative = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True, blank=True, related_name='alternative')
    
class Recette(models.Model):
    nom = models.CharField(max_length=100)
    auteur = models.ForeignKey(Autheur,on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    difficulte = models.IntegerField()
    instruction = models.TextField()
    ingredient = models.ManyToManyField(Ingredient)
    def __str__(self):
        return f'{self.nom}'
    
class RecetteIngredient(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unite = models.CharField(max_length=10, choices=choices , default='g')
    valeur = models.FloatField()