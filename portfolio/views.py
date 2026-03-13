from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import CorteCabello, Musica, MensajeContacto, InformacionPersonal, ImagenHero
from .forms import ContactoForm


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


def contacto(request):
    """Vista para el formulario de contacto"""
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save()
            
            # Enviar email (opcional)
            try:
                send_mail(
                    subject=f'Nuevo mensaje de contacto: {mensaje.asunto}',
                    message=f'De: {mensaje.nombre} ({mensaje.email})\n\n{mensaje.mensaje}',
                    from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else mensaje.email,
                    recipient_list=[settings.EMAIL_HOST_USER] if hasattr(settings, 'EMAIL_HOST_USER') else [],
                    fail_silently=True,
                )
            except:
                pass  # Si falla el email, no es crítico
            
            messages.success(request, '¡Mensaje enviado con éxito! Te contactaremos pronto.')
            return redirect('contacto')
    else:
        form = ContactoForm()
    
    # Obtener información personal para mostrar datos de contacto
    try:
        info_personal = InformacionPersonal.objects.get(pk=1)
    except InformacionPersonal.DoesNotExist:
        info_personal = None
    
    context = {
        'form': form,
        'info_personal': info_personal,
    }
    return render(request, 'portfolio/contacto.html', context)


def sobre_mi(request):
    """Vista para la página 'Sobre Mí'"""
    try:
        info_personal = InformacionPersonal.objects.get(pk=1)
    except InformacionPersonal.DoesNotExist:
        info_personal = None
    
    context = {
        'info_personal': info_personal,
    }
    return render(request, 'portfolio/sobre_mi.html', context)
