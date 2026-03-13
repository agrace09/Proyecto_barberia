# 🎨 Sitio Web de Marca Personal - Barbero & Cantante

Un sitio web profesional desarrollado con Django para mostrar el arte de un barbero y cantante, incluyendo su galería de cortes, música y sistema de contacto.

## 📋 Características

- **Galería de Cortes**: Muestra fotos de cortes de cabello con opción de filtrar por servicio a domicilio
- **Música**: Sección para mostrar canciones, álbumes y videos musicales con enlaces a Spotify, YouTube y SoundCloud
- **Formulario de Contacto**: Sistema completo para recibir mensajes de clientes
- **Sobre Mí**: Página personal con biografía y redes sociales
- **Panel de Administración**: Interfaz Django Admin para gestionar todo el contenido

## 🎨 Ideas de Diseño

### Paleta de Colores
- **Primario**: Negro (#1a1a1a) - Elegancia y profesionalismo
- **Secundario**: Dorado (#d4af37) - Lujo y distinción
- **Acento**: Blanco y grises claros - Contraste y legibilidad

### Estilo Visual
- **Diseño Moderno y Minimalista**: Enfoque en el contenido visual
- **Tipografía**: Poppins (Google Fonts) - Moderna y legible
- **Efectos Hover**: Animaciones sutiles en tarjetas e imágenes
- **Responsive**: Diseño adaptable a móviles, tablets y desktop

### Elementos de Diseño Sugeridos
1. **Hero Section**: Imagen de fondo con texto superpuesto y call-to-action
2. **Galería con Grid**: Mosaico de imágenes con efecto hover
3. **Cards Elevadas**: Tarjetas con sombras y efectos de elevación
4. **Iconografía**: Font Awesome para iconos sociales y de navegación
5. **Badges**: Etiquetas para destacar servicios (ej: "Servicio a Domicilio")

## 📁 Estructura del Proyecto

```
Proyecto_Barberia/
│
├── barberia_project/          # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py            # Configuración de Django
│   ├── urls.py                # URLs principales
│   ├── wsgi.py
│   └── asgi.py
│
├── portfolio/                 # App principal
│   ├── __init__.py
│   ├── models.py             # Modelos de datos
│   ├── views.py              # Vistas (lógica)
│   ├── urls.py               # URLs de la app
│   ├── admin.py              # Configuración del admin
│   ├── forms.py              # Formularios
│   └── apps.py
│
├── templates/                 # Plantillas HTML
│   ├── base.html             # Plantilla base
│   └── portfolio/
│       ├── index.html        # Página principal
│       ├── galeria_cortes.html
│       ├── musica.html
│       ├── contacto.html
│       └── sobre_mi.html
│
├── static/                    # Archivos estáticos (CSS, JS, imágenes)
├── media/                     # Archivos subidos por usuarios
├── manage.py                  # Script de administración Django
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Este archivo
```

## 🚀 Instalación y Configuración

### 1. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear superusuario (para acceder al admin)

```bash
python manage.py createsuperuser
```

### 5. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El sitio estará disponible en: `http://127.0.0.1:8000/`

Panel de administración: `http://127.0.0.1:8000/admin/`

## 📝 Modelos de Datos

### 1. **CorteCabello**
- Almacena fotos de cortes de cabello
- Campos: título, descripción, imagen, fecha, servicio_domicilio, destacado

### 2. **Musica**
- Almacena información sobre música
- Campos: título, tipo (canción/álbum/video), URLs de plataformas, imagen_portada, fecha_lanzamiento

### 3. **MensajeContacto**
- Almacena mensajes del formulario de contacto
- Campos: nombre, email, teléfono, asunto, mensaje, fecha, estado

### 4. **InformacionPersonal**
- Información del barbero/cantante (solo un registro)
- Campos: nombre_artístico, biografía, foto_perfil, contactos, redes sociales

## 🎯 Funcionalidades por Implementar (Opcional)

### Mejoras Futuras Sugeridas:
1. **Sistema de Citas**: Calendario para agendar citas
2. **Blog**: Sección de blog para compartir tips y noticias
3. **Testimonios**: Reseñas de clientes
4. **Galería de Videos**: Videos de cortes en proceso
5. **Multi-idioma**: Soporte para varios idiomas
6. **SEO**: Optimización para motores de búsqueda
7. **Analytics**: Integración con Google Analytics
8. **Newsletter**: Sistema de suscripción por email

## 🎨 Personalización del Diseño

### Cambiar Colores
Edita el archivo `templates/base.html` y modifica las variables CSS:
```css
:root {
    --color-primary: #1a1a1a;    /* Color principal */
    --color-secondary: #d4af37;  /* Color secundario */
}
```

### Agregar Más Secciones
1. Crea una nueva vista en `portfolio/views.py`
2. Agrega la URL en `portfolio/urls.py`
3. Crea el template en `templates/portfolio/`
4. Agrega el enlace en el navbar de `templates/base.html`

## 📧 Configuración de Email (Producción)

Para que el formulario de contacto envíe emails reales, edita `barberia_project/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'tu-password'
DEFAULT_FROM_EMAIL = 'tu-email@gmail.com'
```

## 🔒 Seguridad (Para Producción)

Antes de lanzar a producción:
1. Cambia `SECRET_KEY` en `settings.py`
2. Configura `DEBUG = False`
3. Agrega tu dominio a `ALLOWED_HOSTS`
4. Configura servidor web (Nginx + Gunicorn)
5. Configura HTTPS/SSL
6. Usa variables de entorno para datos sensibles

## 📚 Recursos de Aprendizaje

- [Documentación Django](https://docs.djangoproject.com/)
- [Django Tutorial Oficial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.3/)
- [Font Awesome](https://fontawesome.com/)

## 🤝 Contribuir

Este es un proyecto de aprendizaje. Siéntete libre de:
- Agregar nuevas funcionalidades
- Mejorar el diseño
- Optimizar el código
- Reportar bugs

## 📄 Licencia

Este proyecto es de uso personal/educativo.

---

**¡Buena suerte con tu primer proyecto Django! 🚀**
