from django.urls import include, path
from .views import ListColis, ListPosition

urlpatterns = [
    path('list_colis/', ListColis.as_view(), name='list_colis'),
    path('list_positions/', ListPosition.as_view(), name='list_positions'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]