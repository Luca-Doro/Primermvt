from django.shortcuts import render

from Miapp.models import Familia

# Create your views here.

def mostrar_Familia(request):

    F1=Familia(nombre='Alicia', apellido='Benchetrit' , edad=62, cumpleanios='1960-05-02')
    F2=Familia(nombre='Lena', apellido='Doro' , edad=22, cumpleanios='2000-09-03')
    F3=Familia(nombre='Claudio', apellido='Doro' , edad=61, cumpleanios='1961-09-05')

    return render(request, 'Miapp/Familia.html', {'Familia':[F1,F2,F3]})
    
