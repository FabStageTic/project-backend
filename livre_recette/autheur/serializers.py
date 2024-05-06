from rest_framework import serializers
from .models import *

class AutheurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autheur
        fields = '__all__'