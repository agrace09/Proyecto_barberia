from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import CorteCabello, Musica, MensajeContacto, InformacionPersonal, ImagenHero



def index(request):
    """Vista principal - Página de inicio"""
    cortes_destacados = CorteCabello.objects.filter(destacado=True)[:6]
    musica_destacada = Musica.objects.filter(destacado=True)[:3]
    imagenes_hero = ImagenHero.objects.filter(activa=True).order_by('orden')[:3]
    
    # Obtener información personal (si existe)
    try:
        info_personal = InformacionPersonal.objects.get(pk=1)
    except InformacionPersonal.DoesNotExist:
        info_personal = None
    
    context = {
        'cortes_destacados': cortes_destacados,
        'musica_destacada': musica_destacada,
        'info_personal': info_personal,
        'imagenes_hero': imagenes_hero,
    }
    return render(request, 'portfolio/index.html', context)


def galeria_cortes(request):
    """Vista para mostrar la galería completa de cortes"""
    cortes = CorteCabello.objects.all().order_by('-fecha')
    
    context = {
        'cortes': cortes,
    }
    return render(request, 'portfolio/galeria_cortes.html', context)


def musica(request):
    """Vista para mostrar la música"""
    canciones = Musica.objects.filter(tipo='cancion')
    albumes = Musica.objects.filter(tipo='album')
    videos = Musica.objects.filter(tipo='video')
    
    context = {
        'canciones': canciones,
        'albumes': albumes,
        'videos': videos,
    }
    return render(request, 'portfolio/musica.html', context)
# En portfolio/views.py
def contacto(request):
    """Vista para la página de contacto (Solo botones de redes)"""
    
    # 1. Obtenemos tu Información Personal
    try:
        info_personal = InformacionPersonal.objects.get(pk=1)
    except InformacionPersonal.DoesNotExist:
        info_personal = None
        
    # 2. Obtenemos tus Redes de Contacto (de la clase que acabamos de modificar)
    try:
        redes_contacto = MensajeContacto.objects.get(pk=1)
    except MensajeContacto.DoesNotExist:
        redes_contacto = None
    
    # Pasamos ambas variables a tu HTML
    context = {
        'info_personal': info_personal,
        'redes_contacto': redes_contacto,
    }
    return render(request, 'portfolio/contacto.html', context)

def sobre_mi(request):
    """Vista para la página 'Sobre Mí'"""
    try:
        info_personal = InformacionPersonal.objects.get(pk=1)
    except InformacionPersonal.DoesNotExist:
        info_personal = None

    imagenes_bio = ImagenHero.objects.filter(activa=True).order_by('orden')[:6]

    exitos_list = []
    caracteristicas_list = []
    if info_personal:
        if info_personal.exitos:
            exitos_list = [x.strip() for x in info_personal.exitos.splitlines() if x.strip()]
        if info_personal.caracteristicas:
            caracteristicas_list = [x.strip() for x in info_personal.caracteristicas.splitlines() if x.strip()]

    context = {
        'info_personal': info_personal,
        'imagenes_bio': imagenes_bio,
        'exitos_list': exitos_list,
        'caracteristicas_list': caracteristicas_list,
    }
    return render(request, 'portfolio/sobre_mi.html', context)
