# 📸 Instrucciones para Agregar las 3 Imágenes del Hero

## Pasos para agregar tus imágenes

### 1. Preparar las imágenes
- **Formato**: JPG o PNG
- **Tamaño recomendado**: 1920x1080px o mayor (formato 16:9)
- **Peso**: Optimiza las imágenes para web (máximo 500KB cada una)
- **Nombres sugeridos**: `hero-1.jpg`, `hero-2.jpg`, `hero-3.jpg`

### 2. Guardar las imágenes
1. Crea la carpeta `static/images/` si no existe
2. Guarda tus 3 imágenes allí con los nombres:
   - `static/images/hero-1.jpg`
   - `static/images/hero-2.jpg`
   - `static/images/hero-3.jpg`

### 3. Actualizar el template
Edita el archivo `templates/portfolio/index.html` y busca las líneas que dicen:

```html
<!-- Imagen 1 -->
<div class="hero-image-slide active" style="background-image: url('...');"></div>
<!-- Imagen 2 -->
<div class="hero-image-slide" style="background-image: url('...');"></div>
<!-- Imagen 3 -->
<div class="hero-image-slide" style="background-image: url('...');"></div>
```

Reemplázalas con:

```html
{% load static %}
<!-- Imagen 1 -->
<div class="hero-image-slide active" style="background-image: url('{% static 'images/hero-1.jpg' %}');"></div>
<!-- Imagen 2 -->
<div class="hero-image-slide" style="background-image: url('{% static 'images/hero-2.jpg' %}');"></div>
<!-- Imagen 3 -->
<div class="hero-image-slide" style="background-image: url('{% static 'images/hero-3.jpg' %}');"></div>
```

**Nota**: Asegúrate de agregar `{% load static %}` al inicio del archivo, justo después de `{% extends 'base.html' %}`.

### 4. Verificar
1. Recarga la página (`Ctrl+F5` o `Cmd+Shift+R`)
2. Las imágenes deberían cambiar automáticamente cada 5 segundos
3. Puedes hacer clic en los indicadores en la parte inferior para cambiar manualmente

## Alternativa: Usar URLs directas

Si prefieres usar URLs de imágenes online (como las que compartiste), simplemente reemplaza las URLs en el `style="background-image: url('...')"` con las URLs de tus imágenes.

---

**Tip**: Usa herramientas como [TinyPNG](https://tinypng.com/) para optimizar las imágenes antes de subirlas.
