# TravelBook Pro Mobile v1.0

PWA independiente para iPhone, iPad, Android y navegadores modernos. Todos los datos se guardan en el propio dispositivo; no se envían a ningún servidor.

## Probar e instalar en iPhone

1. Descomprime el paquete y publícalo en una dirección **HTTPS** (por ejemplo, en tu alojamiento web). Para las funciones offline e instalación, no sirve abrir `index.html` directamente desde Archivos.
2. Abre la dirección en Safari en el iPhone.
3. Pulsa **Compartir** y elige **Añadir a pantalla de inicio**.
4. Abre TravelBook desde el icono. Tras la primera carga funcionará sin conexión.

## Datos y copias

Los viajes se guardan localmente en el navegador. En **Más → Copias e importación** descarga una copia JSON antes de cambiar de móvil, borrar Safari o actualizar el sistema. Desde esa misma pantalla puedes restaurarla.

## Exportar

Cada viaje se puede exportar como CSV, compatible con Excel, y como vista de impresión/PDF. En iPhone, la opción PDF abre la hoja de compartir de Safari: usa **Imprimir** y amplía la previsualización para guardarla como PDF, o compártela con Archivos.

## Contenido

- `index.html`, `styles.css`, `app.js`: aplicación sin dependencias externas.
- `manifest.webmanifest`, `service-worker.js`: instalación PWA y funcionamiento offline.
- `assets/icon.svg`: icono de la aplicación.
