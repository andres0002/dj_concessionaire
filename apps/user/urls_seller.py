# django
from django.urls import path
# third
# own
from apps.user.views_seller import ListadoVehiculos, AdicionaVehiculo, VisualizaVehiculo, BorraVehiculo, ModificaVehiculo, ModificaPerfil

urlpatterns = [
    path('listar-vehiculos/', ListadoVehiculos.as_view(), name='listar_vehiculos'),
    path('adicionar-vehiculos/', AdicionaVehiculo.as_view(), name='adicionar_vehiculo'),
    path('visualizar-vehiculos/<slug:id_vehiculo>/', VisualizaVehiculo.as_view(), name='visualizar_vehiculo'),
    path('borrar-vehiculos/<slug:id_vehiculo>/', BorraVehiculo.as_view(), name='borrar_vehiculo'),
    path('modificar-vehiculos/<slug:id_vehiculo>/', ModificaVehiculo.as_view(), name='modificar_vehiculo'),
    path('modificar-perfil/', ModificaPerfil.as_view(), name='modificar_perfil'),
]