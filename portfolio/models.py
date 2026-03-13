from django.db import models
from django.utils import timezone


class CorteCabello(models.Model):
    """Modelo para almacenar fotos de cortes de cabello"""
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    imagen = models.ImageField(upload_to='cortes/', verbose_name='Imagen')
    fecha = models.DateTimeField(default=timezone.now, verbose_name='Fecha')
    servicio_domicilio = models.BooleanField(
        default=False, 
        verbose_name='Servicio a domicilio'
    )
    destacado = models.BooleanField(
        default=False, 
        verbose_name='Destacar en portada'
    )
    
    class Meta:
        verbose_name = 'Corte de Cabello'
        verbose_name_plural = 'Cortes de Cabello'
        ordering = ['-fecha']
    
    def __str__(self):
        return self.titulo


class Musica(models.Model):
    """Modelo para almacenar información sobre música"""
    TIPO_CHOICES = [
        ('cancion', 'Canción'),
        ('album', 'Álbum'),
        ('video', 'Video Musical'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name='Título')
    tipo = models.CharField(
        max_length=20, 
        choices=TIPO_CHOICES, 
        default='cancion',
        verbose_name='Tipo'
    )
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    url_spotify = models.URLField(blank=True, verbose_name='URL Spotify')
    url_youtube = models.URLField(blank=True, verbose_name='URL YouTube')
    url_soundcloud = models.URLField(blank=True, verbose_name='URL SoundCloud')
    imagen_portada = models.ImageField(
        upload_to='musica/', 
        blank=True, 
        verbose_name='Imagen de Portada'
    )
    fecha_lanzamiento = models.DateField(
        default=timezone.now, 
        verbose_name='Fecha de Lanzamiento'
    )
    destacado = models.BooleanField(
        default=False, 
        verbose_name='Destacar en portada'
    )
    
    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Música'
        ordering = ['-fecha_lanzamiento']
    
    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"


class MensajeContacto(models.Model):
    """Modelo para almacenar mensajes del formulario de contacto"""
    ESTADO_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('leido', 'Leído'),
        ('respondido', 'Respondido'),
    ]
    
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    email = models.EmailField(verbose_name='Email')
    telefono = models.CharField(
        max_length=20, 
        blank=True, 
        verbose_name='Teléfono'
    )
    asunto = models.CharField(max_length=200, verbose_name='Asunto')
    mensaje = models.TextField(verbose_name='Mensaje')
    fecha = models.DateTimeField(
        default=timezone.now, 
        verbose_name='Fecha de Envío'
    )
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='nuevo',
        verbose_name='Estado'
    )
    
    class Meta:
        verbose_name = 'Mensaje de Contacto'
        verbose_name_plural = 'Mensajes de Contacto'
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.nombre} - {self.asunto}"


class ImagenHero(models.Model):
    """Modelo para las imágenes del hero section (máximo 3)"""
    imagen = models.ImageField(upload_to='hero/', verbose_name='Imagen')
    orden = models.IntegerField(
        default=1, 
        verbose_name='Orden',
        help_text='Orden de aparición (1, 2 o 3)'
    )
    activa = models.BooleanField(
        default=True, 
        verbose_name='Activa',
        help_text='Mostrar esta imagen en el hero'
    )
    
    class Meta:
        verbose_name = 'Imagen Hero'
        verbose_name_plural = 'Imágenes Hero'
        ordering = ['orden']
    
    def __str__(self):
        return f"Imagen Hero {self.orden}"
    


class InformacionPersonal(models.Model):
    """Modelo para información personal del barbero/cantante (solo un registro)"""
    nombre_artistico = models.CharField(
        max_length=100, 
        verbose_name='Nombre Artístico'
    )
    biografia = models.TextField(verbose_name='Biografía')
    foto_perfil = models.ImageField(
        upload_to='perfil/', 
        verbose_name='Foto de Perfil'
    )
    email_contacto = models.EmailField(verbose_name='Email de Contacto')
    telefono_contacto = models.CharField(
        max_length=20, 
        verbose_name='Teléfono de Contacto'
    )
    direccion = models.TextField(blank=True, verbose_name='Dirección')
    instagram = models.URLField(blank=True, verbose_name='Instagram')
    facebook = models.URLField(blank=True, verbose_name='Facebook')
    twitter = models.URLField(blank=True, verbose_name='Twitter')
    youtube = models.URLField(blank=True, verbose_name='YouTube')
    spotify = models.URLField(blank=True, verbose_name='Spotify')
    
    class Meta:
        verbose_name = 'Información Personal'
        verbose_name_plural = 'Información Personal'
    
    def __str__(self):
        return self.nombre_artistico
    
    def save(self, *args, **kwargs):
        # Asegurar que solo haya un registro
        self.pk = 1
        super().save(*args, **kwargs)
