from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import *

# Create your views here.
class ColiViewSet(viewsets.ModelViewSet):
    queryset = Coli.objects.all()
    serializer_class = ColiSerializer
    permission_classes = [ColiReadWritePermission]
    
class PositionViewSet(viewsets.ModelViewSet):
    
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [PositionReadWritePermission]