from .models import *
from rest_framework import serializers


class ColiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coli
        fields = ['client', 'numeros_colis']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
        # fields = ['location','coli']

        # depth = 1
