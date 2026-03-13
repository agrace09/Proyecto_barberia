from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria/', views.galeria_cortes, name='galeria_cortes'),
    path('musica/', views.musica, name='musica'),
    path('contacto/', views.contacto, name='contacto'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
]
