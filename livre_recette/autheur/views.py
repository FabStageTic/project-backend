from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.


class AutheurViewset(viewsets.ModelViewSet):
    
    queryset = Autheur.objects.all()
    serializer_class = AutheurSerializer
