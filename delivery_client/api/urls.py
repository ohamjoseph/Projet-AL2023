from django.urls import include, path
from .views import ListColis

urlpatterns = [
    path('list_colis/', ListColis.as_view(), name='list_colis'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]