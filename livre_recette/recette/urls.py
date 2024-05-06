from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'recette', views.RecetteViewset)
router.register(r'ingredient', views.IngredientViewset)
router.register(r'quantite', views.RecetteIngredientViewset)

urlpatterns = [
    path('', include(router.urls)),
]