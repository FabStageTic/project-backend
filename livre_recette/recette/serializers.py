from rest_framework import serializers
from collections import OrderedDict
from .models import *


class RecetteSerializer(serializers.HyperlinkedModelSerializer):
#    ingredient_id = serializers.PrimaryKeyRelatedField(
#        many=True,
#        queryset = Ingredient.objects.all(),
#        
#    )
#    ingredient = serializers.HyperlinkedRelatedField(
#        many=True,
#        read_only =True,
#        view_name='ingredient-detail'
#    )
    #tracks = RecetteIngredientSerializer(many=True, read_only=True)
    
    class Meta:
        model = Recette
        fields = ['url','nom', 'auteur', 'description', 'difficulte', 'instruction', 'ingredient']
        
class IngredientSerializer(serializers.HyperlinkedModelSerializer):
#    variete_id = serializers.PrimaryKeyRelatedField(
#        many=True,
#        queryset = Ingredient.objects.all(),
#        write_only = True,
#    )
#    variete = serializers.HyperlinkedRelatedField(
#        many=True,
#        read_only = True,
#        view_name='ingredient-detail'
#        
#    )
    alternatives = serializers.StringRelatedField(many=True)
    class Meta:
        model = Ingredient
        fields = ['nom', 'alternatives']
    def to_representation(self, instance):
        result = super(IngredientSerializer, self).to_representation(instance)
        return OrderedDict([([key, result[key]]) for key in result if result[key] is not None])

#    variete_id = serializers.PrimaryKeyRelatedField(
#        many=True,
#        queryset= Ingredient.objects.get('nom'),
#        write_only = True
#    )
#    variete = serializers.HyperlinkedRelatedField(
#        many=True,
#        read_only=True,
#        view_name='ingredient-detail'
#    )
#    
#    class Meta: 
#        model = Ingredient
#        fields = '__all__'
class RecetteIngredientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RecetteIngredient
        fields = ['recette','ingredient','unite','valeur']
        
    def get_combined_ingredient(self, obj):
        return f"{obj.ingredient.nom} ({obj.unite})"