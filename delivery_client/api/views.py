import requests
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import decorators
from api import tools


class ListColis(APIView):
    def get(self, request):
        response = {}
        numero = request.GET.get('q', None)
        if numero is not None:
            colis_data = requests.get(tools.coli_url, params={"q": numero}).json()
        else:
            colis_data = requests.get(tools.coli_url).json()

        # Traitement des données et formatage
        if len(colis_data) == 0:
            response['error'] = True
            response['error_field'] = "Ce coli n'existe pas ou erreur de numero"
            
        response['colis_data'] = colis_data

        # Renvoi des données agrégées sous forme de réponse HTTP
        return Response(response)

    def post(self, request):
        list_colis = {}
        
        data = request.data
        coli = {
            'client': data['client'],
            'numeros_colis': data['numero'],
        }

        response_coli = requests.post(tools.coli_url, json=coli)
        
        print('dfgyhythtyh', response_coli.ok)
        if not response_coli.ok:
            response_coli = response_coli.json()
            
            list_colis['error'] = True
            list_colis['error_field'] = response_coli['numeros_colis'][0]
            return Response(list_colis)
        
        else:
            location = data['latitude'] + ',' + data['longitude']
            position = {
                'location': location,
                'coli': data['numero']
            }
            response_position = requests.post(tools.posotion_url, json=position)

            if not response_position.ok:
                response_position = response_position.json()
            
            list_colis['position_data'] = response_position

        list_colis = {
            'colis_data': response_coli,
            'position_data': response_position,
        }

        return Response(list_colis)


class ListPosition(APIView):
    def get(self, request):
        numero = request.GET.get('q', None)
        if numero is not None:
            position_data = requests.get(tools.posotion_url, params={"q": numero})
        else:
            position_data = requests.get(tools.posotion_url)

        # Traitement des données et formatage
        list_colis = {
            'colis_data': position_data.json(),
        }

        # Renvoi des données agrégées sous forme de réponse HTTP
        return Response(list_colis)

    def post(self, request):
        data = request.data

        location = data['latitude'] + ',' + data['longitude']
        position = {
            'location': location,
            'coli': data['numero']
        }
        response_position = requests.post(tools.posotion_url, json=position)

        if not response_position.ok:
            response_position = response_position.json()

        list_colis = {
            'position_data': response_position.json(),
        }

        return Response(list_colis)
