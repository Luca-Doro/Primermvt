from django.urls import path

from Miapp.views import mostrar_Familia

urlpatterns = [
    path('', mostrar_Familia)
]
