import requests
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import decorators
from api import tools

class ListColis(APIView):
    def get(self, request):
        numero = request.GET.get('numero',None)
        if numero is not None:
            colis_data = requests.get(tools.coli_url,params={"numero": numero})
        else:
            colis_data = requests.get(tools.coli_url)
            
        # Traitement des données et formatage
        list_colis = {
            'colis_data': colis_data.json(),
        }
        
        # Renvoi des données agrégées sous forme de réponse HTTP
        return Response(list_colis)
    
    def post(self, request):
        data = request.data
        
        response = requests.post(tools.coli_url, json=data)
        if not response.ok:
            response = response.json()
        
        list_colis = {
            'colis_data': response,
        }
        
        return Response(list_colis)
        