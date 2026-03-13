# 🚀 Guía de Inicio Rápido

## Pasos para comenzar

### 1. Instalar Python
Asegúrate de tener Python 3.8 o superior instalado.

### 2. Crear y activar entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Django y dependencias
```bash
pip install -r requirements.txt
```

### 4. Crear las tablas de la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear un usuario administrador
```bash
python manage.py createsuperuser
```
Sigue las instrucciones para crear tu usuario y contraseña.

### 6. Ejecutar el servidor
```bash
python manage.py runserver
```

### 7. Abrir en el navegador
- **Sitio web**: http://127.0.0.1:8000/
- **Panel de administración**: http://127.0.0.1:8000/admin/

## 📝 Primeros pasos después de iniciar

1. **Accede al panel de administración** con el usuario que creaste
2. **Agrega tu información personal**:
   - Ve a "Información Personal" y completa tu perfil
3. **Agrega algunos cortes de cabello**:
   - Ve a "Cortes de Cabello" y agrega fotos
   - Marca algunos como "Destacado" para que aparezcan en la portada
4. **Agrega tu música**:
   - Ve a "Música" y agrega tus canciones/álbumes
   - Incluye los enlaces de Spotify, YouTube, etc.
5. **Personaliza el diseño**:
   - Edita `templates/base.html` para cambiar colores y estilos
   - Agrega tu logo si lo tienes

## 🎨 Personalización rápida

### Cambiar el nombre del sitio
Edita `templates/base.html` línea 6:
```html
<title>{% block title %}TU NOMBRE - Barbero & Cantante{% endblock %}</title>
```

### Cambiar colores
Edita `templates/base.html` en la sección `<style>`:
```css
:root {
    --color-primary: #TU_COLOR;    /* Color principal */
    --color-secondary: #TU_COLOR;   /* Color secundario */
}
```

## ⚠️ Notas importantes

- Las imágenes se guardan en la carpeta `media/`
- El formulario de contacto guarda los mensajes en la base de datos
- Para producción, configura el email en `barberia_project/settings.py`
- Cambia `SECRET_KEY` y `DEBUG = False` antes de lanzar a producción

## 🆘 Problemas comunes

**Error: "No module named 'django'"**
- Asegúrate de haber activado el entorno virtual
- Ejecuta: `pip install -r requirements.txt`

**Error al subir imágenes**
- Asegúrate de que la carpeta `media/` existe
- Verifica que Pillow está instalado: `pip install Pillow`

**No puedo acceder al admin**
- Verifica que creaste el superusuario: `python manage.py createsuperuser`
- Asegúrate de usar la URL correcta: `/admin/`

---

¡Disfruta construyendo tu sitio web! 🎉
