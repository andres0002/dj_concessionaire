# django
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# third
# own
from apps.user.models import UsuarioRol

# Create your views here.

class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get("signin_username", "")
        password = request.POST.get("signin_password", "")
        usuario = auth.authenticate(username=username,
                                    password=password)
        if usuario != None and usuario.is_active:
            auth.login(request, usuario)
            lista_roles = UsuarioRol.objects.filter(usuid=usuario.pk)

            if len(lista_roles) > 0:
                if lista_roles[0].rolid.roltipo == "seller":
                    return HttpResponseRedirect(reverse('user:seller:listar_vehiculos'))

                elif lista_roles[0].rolid.roltipo == "buyer":
                    return HttpResponseRedirect(reverse('user:buyer:listar_vehiculos'))

                else:
                    messages.add_message(request, messages.ERROR, "Rol de usuario inexistente")

            else:
                messages.add_message(request, messages.ERROR, "El Usuario no tiene roles asignados")

        else:
            if usuario == None:
                messages.add_message(request, messages.ERROR, "El Usuario no existe en el Sistema")

            else:
                messages.add_message(request, messages.ERROR, "El Usuario esta inactivo")

        return render(request, 'login.html')

class Logout(View):
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('login'))