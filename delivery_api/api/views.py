from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from .permissions import *

# Create your views here.

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [PositionReadWritePermission]