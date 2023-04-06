from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics

from .models import *
from .serializers import *
from .permissions import *

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
class ColiViewSet(viewsets.ModelViewSet):
    queryset = Coli.objects.all()
    serializer_class = ColiSerializer
    permission_classes = [ColiReadWritePermission]

    def get_queryset(self):
        queryset = Coli.objects.all()
        numero = self.request.GET.get('numero')
        if numero is not None:
            queryset = queryset.filter(numeros_colis=numero)
        return queryset


class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    permission_classes = [PositionReadWritePermission]
    queryset = Position.objects.all()

    def get_queryset(self):
        queryset = Position.objects.all()
        coli = self.request.GET.get('coli')
        if coli is not None:
            queryset = queryset.filter(coli__numeros_colis=coli)
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        new_position = Position.objects.create(location=data["location"],
                                               coli=Coli.objects.get(numeros_colis=data['coli']))

        new_position.save()
        serializer = PositionSerializer(new_position)

        return Response(serializer.data)
