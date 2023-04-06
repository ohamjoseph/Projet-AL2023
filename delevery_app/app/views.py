from django.shortcuts import render
import requests
from .tools import client_api
from .forms import Address


# Create your views here.
def home(request):
    context = {}
    if request.method == 'POST':
        numero = request.POST.get('numero', None)
        positions = requests.get(client_api + 'client/list_positions', params={'q': numero})
        positions = positions.json()['colis_data']
        for idx, val in enumerate(positions):
            latitude, longitude = val['location'].split(',')
            positions[idx]['latitude'] = latitude
            positions[idx]['longitude'] = longitude
        context = {'positions': positions,
                   'latitude': positions[-1]['latitude'],
                   'longitude': positions[-1]['longitude']}

    return render(request, 'app/home.html', context=context)


def signe(request):
    return render(request, 'app/new.html')

def addresses(request):
    form = Address()
    return render(request, 'app/address.html', {'form': form})


