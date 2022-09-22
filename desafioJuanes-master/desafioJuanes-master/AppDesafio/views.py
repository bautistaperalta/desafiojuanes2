from django.shortcuts import render
from django.http import HttpResponse
from AppDesafio.models import Datos_registro

# Create your views here.

def registro(request):
    if request.method == "POST":
        estudiante = Datos_registro(nombre_completo = request.POST['nombre_completo'], fechaDeNacimiento = request.POST['fechaDeNacimiento'], email = request.POST['email'], contraseña = request.POST['contraseña'])
        estudiante.save()
        return render(request, "home.html")
    return render(request, "registro.html")
