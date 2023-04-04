from .models import *
from rest_framework import serializers

class ColiSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Coli
        fields = ['client','numeros_colis','location']
class PositionSerializer(serializers.HyperlinkedModelSerializer):
    coli = serializers.CharField(source='coli.numeros_colis')
    class Meta:
        model = Position
        fields = ['location','coli']