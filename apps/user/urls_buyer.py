# django
from django.urls import path
# third
# own
from apps.user.views_buyer import ListadoVehiculos, ModificaPerfil, VisualizaPerfilVendedor, VisualizaVehiculo

urlpatterns = [
    path('listar-vehiculos/', ListadoVehiculos.as_view(), name='listar_vehiculos'),
    path('modificar-perfil/', ModificaPerfil.as_view(), name='modificar_perfil'),
    path('perfil-vendedor/<int:id_vendedor>/', VisualizaPerfilVendedor.as_view(), name='visualizar_perfil_vendedor'),
    path('visualizar-vehiculos/<slug:id_vehiculo>/', VisualizaVehiculo.as_view(), name='visualizar_vehiculo'),
]