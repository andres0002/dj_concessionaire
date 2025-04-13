# django
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# third
# own
from apps.user.models import DatosPersonales, Vehiculo
from apps.user.forms import DatosPersonalesForm, VehiculoForm

# Create your views here.

class ListadoVehiculos(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'seller/listar_vehiculos.html'

    def get(self, request):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            lista_vehiculos = Vehiculo.objects.filter(datid=datos_usuario.pk)
            return render(request,
                self.template_name,
                {
                    'vehiculos': lista_vehiculos,
                    'foto_usuario': datos_usuario.foto
                }
            )

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")


class AdicionaVehiculo(LoginRequiredMixin, View):
    login_url = '/'
    form_class = VehiculoForm
    template_name = 'seller/adicionar_vehiculo.html'

    def get(self, request):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            form = self.form_class(datos_usuario)
            return render(request,
                self.template_name,
                {
                    'form': form,
                    'foto_vehiculo': None,
                    'foto_usuario': datos_usuario.foto
                }
            )

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            form = self.form_class(datos_usuario, request.POST, request.FILES)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Vehículo se adicionó correctamente')

            else:
                messages.add_message(request, messages.ERROR, 'El Vehículo no se pudo adicionar')

            listar = ListadoVehiculos()
            return listar.get(request)

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")


class VisualizaVehiculo(LoginRequiredMixin, View):
    login_url = '/'
    form_class = VehiculoForm
    template_name = 'seller/visualizar_vehiculo.html'

    def get(self, request, id_vehiculo):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            vehiculo = Vehiculo.objects.get(vehplaca=id_vehiculo)
            form = self.form_class(datos_usuario, instance=vehiculo)
            return render(request,
                self.template_name,
                {
                'form': form,
                'foto_vehiculo': vehiculo.vehfoto,
                'foto_usuario': datos_usuario.foto
                }
            )

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")

        except Vehiculo.DoesNotExist:
            return render(request, "pages-404.html")


class BorraVehiculo(LoginRequiredMixin, View):
    login_url = '/'
    form_class = VehiculoForm
    template_name = 'seller/borrar_vehiculo.html'

    def get(self, request, id_vehiculo):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            vehiculo = Vehiculo.objects.get(vehplaca=id_vehiculo)
            form = self.form_class(datos_usuario, instance=vehiculo)
            return render(request,
                self.template_name,
                {
                    'form': form,
                    'foto_vehiculo': vehiculo.vehfoto,
                    'foto_usuario': datos_usuario.foto
                }
            )

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")

        except Vehiculo.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request, id_vehiculo):
        try:
            vehiculo = Vehiculo.objects.get(vehplaca=id_vehiculo)
            vehiculo.delete()
            messages.add_message(request, messages.INFO, "El Vehículo se borró correctamente")
            listar = ListadoVehiculos()
            return listar.get(request)

        except Vehiculo.DoesNotExist:
            return render(request, "pages-404.html")


class ModificaVehiculo(LoginRequiredMixin, View):
    login_url = '/'
    form_class = VehiculoForm
    template_name = 'seller/modificar_vehiculo.html'

    def get(self, request, id_vehiculo):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            vehiculo = Vehiculo.objects.get(vehplaca=id_vehiculo)
            form = self.form_class(datos_usuario, instance=vehiculo)
            return render(request,
                self.template_name,
                {
                    'form': form,
                    'foto_vehiculo': vehiculo.vehfoto,
                    'foto_usuario': datos_usuario.foto
                }
            )

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")

        except Vehiculo.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request, id_vehiculo):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            vehiculo = Vehiculo.objects.get(vehplaca=id_vehiculo)
            form = self.form_class(datos_usuario, request.POST, request.FILES, instance=vehiculo)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Vehículo se modificó correctamente')

            else:
                messages.add_message(request, messages.ERROR, 'El Vehículo no se pudo modificar')

            listar = ListadoVehiculos()
            return listar.get(request)

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")

        except Vehiculo.DoesNotExist:
            return render(request, "pages-404.html")


class ModificaPerfil(LoginRequiredMixin, View):
    login_url = '/'
    form_class = DatosPersonalesForm
    template_name = 'seller/perfil_vendedor.html'

    def get(self, request):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            form = self.form_class(request.user, instance=datos_usuario)
            return render(request,
                self.template_name,
                {
                    'form': form,
                    'foto_usuario': datos_usuario.foto
                }
            )

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            form = self.form_class(request.user, request.POST, request.FILES, instance=datos_usuario)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Perfil se modificó correctamente')

            else:
                messages.add_message(request, messages.ERROR, 'El Perfil no se pudo modificar')

            return self.get(request)

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")