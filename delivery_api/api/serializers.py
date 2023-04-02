from .models import *
from rest_framework import serializers

class ColiSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Coli
        fields = '__all__'
        
class PositionSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Position
        fields = ['location']
