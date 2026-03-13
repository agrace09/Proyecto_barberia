# 📸 Guía Rápida: Agregar Imágenes al Hero

## Pasos para agregar tus 3 imágenes

### 1. Acceder al Admin
1. Ve a: `http://127.0.0.1:8000/admin/`
2. Inicia sesión con tu usuario administrador

### 2. Agregar las Imágenes
1. En el menú lateral, busca **"Imágenes Hero"**
2. Haz clic en **"Añadir Imagen Hero"**
3. Sube tu primera imagen
4. Establece el **Orden** a `1`
5. Marca **"Activa"** como activado
6. Guarda

### 3. Repetir para las otras 2 imágenes
- Segunda imagen: **Orden** = `2`
- Tercera imagen: **Orden** = `3`
- Ambas con **"Activa"** marcado

### 4. Verificar
1. Ve a la página principal: `http://127.0.0.1:8000/`
2. Las imágenes deberían aparecer en el hero section
3. El carrusel cambiará automáticamente cada 5 segundos

## Características

- ✅ Máximo 3 imágenes activas (puedes tener más, pero solo 3 se mostrarán)
- ✅ Orden personalizable (1, 2, 3)
- ✅ Puedes activar/desactivar imágenes sin eliminarlas
- ✅ Carrusel automático con transiciones suaves
- ✅ Indicadores clicables en la parte inferior

## Tips

- **Tamaño recomendado**: 1920x1080px (formato 16:9)
- **Peso**: Optimiza las imágenes antes de subirlas (máximo 500KB cada una)
- **Formato**: JPG o PNG
- **Contenido**: Las imágenes deben tener buena calidad y ser representativas de tu marca

---

**¡Listo!** Ahora puedes gestionar las imágenes del hero directamente desde el admin de Django. 🎨
