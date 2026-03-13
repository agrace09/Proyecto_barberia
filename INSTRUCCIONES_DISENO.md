# 🎨 Instrucciones para Personalizar el Diseño

## Imágenes de Fondo

El diseño actual usa imágenes de Unsplash como placeholders. Para personalizar:

### 1. Hero Section (Página Principal)
- **Ubicación**: `templates/portfolio/index.html`
- **Línea**: `.hero-background`
- **Recomendación**: Imagen que muestre al barbero/cantante en ambas actividades (música y barbería)
- **Tamaño recomendado**: 1920x1080px o mayor
- **Formato**: JPG o PNG

**Para agregar tu imagen:**
1. Guarda tu imagen en `static/images/hero-bg.jpg`
2. En `index.html`, cambia:
```html
<div class="hero-background" style="background-image: url('{% static 'images/hero-bg.jpg' %}');"></div>
```

### 2. Panel de Música
- **Ubicación**: `templates/portfolio/index.html`
- **Línea**: Panel izquierdo con clase `feature-panel`
- **Recomendación**: Imagen del artista cantando o con micrófono
- **Tamaño recomendado**: 1200x800px

**Para agregar tu imagen:**
1. Guarda en `static/images/music-bg.jpg`
2. Cambia el `style="background-image: url('...')"` en el panel de música

### 3. Panel de Barbería
- **Ubicación**: `templates/portfolio/index.html`
- **Línea**: Panel derecho con clase `feature-panel`
- **Recomendación**: Imagen cortando cabello o del espacio de trabajo
- **Tamaño recomendado**: 1200x800px

**Para agregar tu imagen:**
1. Guarda en `static/images/barberia-bg.jpg`
2. Cambia el `style="background-image: url('...')"` en el panel de barbería

## Colores Personalizados

Para cambiar los colores, edita `templates/base.html` en la sección `:root`:

```css
:root {
    --color-primary: #0a0a0a;      /* Fondo principal (negro) */
    --color-secondary: #c9a961;    /* Dorado/ámbar principal */
    --color-accent: #d4af37;        /* Dorado más brillante */
    --color-text: #ffffff;          /* Texto blanco */
    --color-text-muted: rgba(255, 255, 255, 0.7); /* Texto gris claro */
}
```

## Tipografía

El diseño usa dos fuentes de Google Fonts:
- **Playfair Display**: Para títulos (serif elegante)
- **Inter**: Para texto del cuerpo (sans-serif moderna)

Para cambiar las fuentes, edita la línea en `base.html`:
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

## Efectos Visuales

### Efecto de Humo/Niebla
El hero section tiene un efecto animado. Para desactivarlo, elimina el bloque `::after` en el CSS de `index.html`.

### Parallax (Efecto de profundidad)
Los paneles de características usan `background-attachment: fixed` para efecto parallax. En móviles se desactiva automáticamente.

## Textos Personalizables

### Hero Section
- **Título principal**: "Todo es arte." (línea 8 en `index.html`)
- **Subtítulo**: "MÚSICA · BARBERÍA · ESTILO" (línea 9)
- **Botones**: "Explorar el arte" y "Visitar la barbería"

### Sección de Filosofía
- **Título**: "El arte se vive." (línea 18)
- **Texto**: Edita el párrafo en la línea 19-22

### Paneles
- **Música**: Título y descripción en líneas 30-33
- **Barbería**: Título y descripción en líneas 44-47

## Agregar Imágenes Propias

1. Crea la carpeta `static/images/` si no existe
2. Sube tus imágenes allí
3. En los templates, usa:
```django
{% load static %}
<img src="{% static 'images/tu-imagen.jpg' %}" alt="Descripción">
```

O para CSS:
```css
background-image: url('{% static 'images/tu-imagen.jpg' %}');
```

## Notas Importantes

- Las imágenes grandes pueden afectar el tiempo de carga. Optimiza las imágenes antes de subirlas.
- Usa herramientas como TinyPNG o ImageOptim para comprimir imágenes.
- El diseño es responsive, pero verifica cómo se ven las imágenes en móviles.
- Los colores dorados (#c9a961, #d4af37) son clave para mantener la identidad visual del diseño.

---

**¡Disfruta personalizando tu sitio!** 🎨
