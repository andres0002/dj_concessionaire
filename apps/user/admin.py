# django
from django.contrib import admin
# third
# own
from apps.user.models import Categoria, DatosPersonales, Rol, UsuarioRol, Vehiculo

# Register your models here.

admin.site.register(Categoria)
admin.site.register(DatosPersonales)
admin.site.register(Rol)
admin.site.register(UsuarioRol)

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('vehplaca', 'datid', 'catid', 'vehmodelo', 'vehmarca', 'vehprecio')
    list_filter = ('vehplaca', 'vehmodelo', 'vehmarca')
    search_fields = ('vehplaca', 'vehmarca')
    ordering = ('vehmodelo',)

admin.site.register(Vehiculo, VehiculoAdmin)