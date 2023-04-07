from django.shortcuts import render
import requests
from .tools import client_api
from .forms import Address

import sweetify

def split_location(positions):
    context = {}
    positions = positions.json()['colis_data']
    if len(positions)!=0:
        for idx, val in enumerate(positions):
            latitude, longitude = val['location'].split(',')
            positions[idx]['latitude'] = latitude
            positions[idx]['longitude'] = longitude
        context = {'positions': positions,
                    'latitude': positions[-1]['latitude'],
                    'longitude': positions[-1]['longitude']}            
    return context
    

# Create your views here.
def home(request):
    context = {}
    if request.method == 'POST':
        numero = request.POST.get('numero', None)
        positions = requests.get(client_api + 'client/list_positions', params={'q': numero})
        context = split_location(positions)
        positions = positions.json()['colis_data']
        if len(positions)==0:
            sweetify.error(request, "Ce colis n'est pas enregisté ou n'est pas de position connues")
        context['data'] = numero

    return render(request, 'app/home.html', context=context)

def signe(request):
    return render(request, 'app/new.html')

def addresses(request):
    data = {}
    context = {}
    if request.method == 'POST':
        
        data['latitude'] = request.POST.get('latitude', None)
        data['longitude'] = request.POST.get('longitude', None)
        data['numero'] = request.POST.get('numero', None)
        aj = request.POST.get('aj', '0')
        if aj == '0':
            response = requests.post(client_api+'client/list_positions/', json=data)
            if response.ok:
                positions = requests.get(client_api + 'client/list_positions', params={'q': data['numero']})
                context = split_location(positions)
                context['data'] = data['numero']
                return render(request, 'app/home.html', context=context)
            else:
                sweetify.error(request, "Ce colis n'a pas encors été enregisté")
                return render(request, 'app/new.html')
        elif aj=='1':
            data['client'] = 1
            response = requests.post(client_api+'client/list_colis/', json=data).json()
            if 'error' in response:
                sweetify.error(request, response['error_field'])
            else :
                positions = requests.get(client_api + 'client/list_positions', params={'q': data['numero']})
                context = split_location(positions)
                sweetify.success(request, 'Le coli n'+data['numero']+' à bien éte ajouté avec succès')
                context['data'] = data['numero']
                return render(request, 'app/home.html', context=context)
        context['data'] = data['numero']
    print(data)
    return render(request, 'app/new.html')


