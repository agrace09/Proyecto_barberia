from django.contrib import admin
from .models import CorteCabello, Musica, MensajeContacto, InformacionPersonal, ImagenHero


@admin.register(CorteCabello)
class CorteCabelloAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'servicio_domicilio', 'destacado']
    list_filter = ['fecha', 'servicio_domicilio', 'destacado']
    search_fields = ['titulo', 'descripcion']
    date_hierarchy = 'fecha'


@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'fecha_lanzamiento', 'destacado']
    list_filter = ['tipo', 'fecha_lanzamiento', 'destacado']
    search_fields = ['titulo', 'descripcion']


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'asunto', 'fecha', 'estado']
    list_filter = ['estado', 'fecha']
    search_fields = ['nombre', 'email', 'asunto', 'mensaje']
    readonly_fields = ['fecha']
    date_hierarchy = 'fecha'


@admin.register(ImagenHero)
class ImagenHeroAdmin(admin.ModelAdmin):
    list_display = ['imagen_preview', 'orden', 'activa']
    list_editable = ['orden', 'activa']
    list_filter = ['activa']
    ordering = ['orden']
    list_display_links = ['imagen_preview']
    
    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" style="max-width: 100px; max-height: 100px;" />'
        return "Sin imagen"
    imagen_preview.allow_tags = True
    imagen_preview.short_description = 'Imagen'


@admin.register(InformacionPersonal)
class InformacionPersonalAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre_artistico', 'biografia', 'foto_perfil')
        }),
        ('Contacto', {
            'fields': ('email_contacto', 'telefono_contacto', 'direccion')
        }),
        ('Redes Sociales', {
            'fields': ('instagram', 'facebook', 'twitter', 'youtube', 'spotify')
        }),
    )
