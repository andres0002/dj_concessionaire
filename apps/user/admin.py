# django
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# third
# own
from apps.user.models import Categoria, DatosPersonales, Rol, UsuarioRol, Vehiculo

# Register your models here.

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria
        import_id_fields = ['catid']

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('catid', 'catipo', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('vehplaca', 'vehmarca')
    ordering = ('catipo',)
    resource_class = CategoriaResource

class DatosPersonalesResource(resources.ModelResource):
    class Meta:
        model = DatosPersonales
        import_id_fields = ['datid']

class DatosPersonalesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('datnombre', 'datapellido', 'datipoid', 'datnumeroid', 'datelefono', 'datcorreo', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('datnombre', 'datapellido')
    ordering = ('datnombre',)
    resource_class = DatosPersonalesResource

class RolResource(resources.ModelResource):
    class Meta:
        model = Rol
        import_id_fields = ['rolid']

class RolAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('roltipo',)
    list_display = ('roltipo', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    ordering = ('roltipo',)
    resource_class = RolResource

class UsuarioRolResource(resources.ModelResource):
    class Meta:
        model = UsuarioRol

class UsuarioRolAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('rolid', 'usuid', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    ordering = ('rolid',)
    resource_class = UsuarioRolResource

class VehiculoResource(resources.ModelResource):
    class Meta:
        model = Vehiculo
        import_id_fields = ['vehplaca']

class VehiculoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('vehplaca', 'datid', 'catid', 'vehmodelo', 'vehmarca', 'vehprecio')
    list_filter = ('vehplaca', 'vehmodelo', 'vehmarca')
    search_fields = ('vehplaca', 'vehmarca')
    ordering = ('vehmodelo',)
    resource_class = VehiculoResource

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(DatosPersonales, DatosPersonalesAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(UsuarioRol, UsuarioRolAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)