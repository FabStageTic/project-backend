from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class RecetteViewset(viewsets.ModelViewSet):
    
    queryset = Recette.objects.all()
    serializer_class = RecetteSerializer
    
class IngredientViewset(viewsets.ModelViewSet):
    
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
class RecetteIngredientViewset(viewsets.ModelViewSet):
    
    queryset = RecetteIngredient.objects.all()
    serializer_class= RecetteIngredientSerializer
    
#def recette_ingredient(request, pk):
#    recette = Recette.objects.get(pk=pk)
#    ingredient = Ingredient.objects.filter(recette=recette)
#    return ingredient