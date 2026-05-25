# Setup Maestro de Marketing Digital — dralbenrosas.com
*Creado: 2026-05-25 | Estado: En progreso*

> **Cómo usar este documento:**
> Sigue los pasos en orden. Cada paso indica claramente:
> - 👤 **TÚ** — lo haces en tu computadora/teléfono
> - 🤖 **YO** — lo configuro yo una vez que me des el ID correspondiente
>
> Al terminar tendrás: GTM + GA4 + Meta Pixel + conversiones de WhatsApp/llamada + dominio verificado + SEO básico + sitio listo para Google Ads y Meta Ads.

---

## IDs QUE NECESITO DE TI

Llena esta tabla a medida que creas las cuentas. Compártela conmigo y configuro todo.

| ID | Dónde encontrarlo | Tu valor |
|----|-------------------|---------|
| GTM Container ID | tagmanager.google.com → tu contenedor → esquina superior derecha | `GTM-_______` |
| GA4 Measurement ID | analytics.google.com → Admin → Flujos de datos → tu sitio | `G-__________` |
| Meta Pixel ID | business.facebook.com → Fuentes de datos → Píxeles | `3456701621158975` ✅ |
| Meta Business ID | business.facebook.com → Configuración → Info del negocio → ID del negocio | `2482834265523958` ✅ |
| Google Ads Conversion ID | Google Ads → Herramientas → Conversiones → tu conversión → ver etiqueta | `AW-__________` |
| Google Ads Conversion Label | Misma pantalla que arriba | `________________` |

---

## PASO 1 — GTM: Crear y configurar el contenedor

### 👤 Tú haces:

1. Ve a **tagmanager.google.com**
2. Inicia sesión con alben.rosas@gmail.com
3. Clic en **"Crear cuenta"**:
   - Nombre de cuenta: `Dr. Alben Rosas`
   - País: `México`
   - Nombre del contenedor: `dralbenrosas.com`
   - Plataforma: **Web**
4. Acepta los Términos de Servicio
5. GTM te muestra una ventana con 2 snippets — ciérrala por ahora (los instalamos en Netlify, no aquí)
6. **Copia tu Container ID** — está en la esquina superior derecha de la pantalla, formato `GTM-XXXXXXX`

**Tiempo estimado: 5 minutos**

---

## PASO 2 — GTM: Instalar en Netlify (Snippet Injection)

### 👤 Tú haces:

1. Ve a **app.netlify.com** → entra a tu sitio `dralbenrosas`
2. Clic en **"Site configuration"** (menú izquierdo)
3. Clic en **"Build & deploy"** → desplázate hacia abajo hasta **"Post processing"**
4. Busca **"Snippet injection"** → clic en **"Add snippet"**

**Snippet #1 — para el `<head>`:**
- Nombre: `GTM - Head`
- Posición: **Before `</head>`**
- Contenido:
```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
<!-- End Google Tag Manager -->
```

5. Clic en **"Add snippet"** nuevamente para el segundo:

**Snippet #2 — para el `<body>`:**
- Nombre: `GTM - Body`
- Posición: **After `<body>`**
- Contenido:
```html
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```

6. Guarda los cambios

> ⚠️ **Importante:** En ambos snippets reemplaza `GTM-XXXXXXX` con tu Container ID real (el que copiaste en el Paso 1).

**Tiempo estimado: 5 minutos**

### Verificar que GTM está instalado:
1. Descarga la extensión **"Tag Assistant Companion"** en Chrome: busca en Google "Tag Assistant Chrome extension"
2. Visita **dralbenrosas.com**
3. Activa Tag Assistant → debe aparecer GTM en verde ✅

---

## PASO 3 — GA4: Crear propiedad

### 👤 Tú haces:

1. Ve a **analytics.google.com**
2. Inicia sesión con alben.rosas@gmail.com
3. Clic en **"Empezar a medir"** (o "Crear propiedad" si ya tienes cuenta)
4. Nombre de la propiedad: `dralbenrosas.com`
5. País: `México` | Moneda: `MXN` | Zona horaria: `México - Ciudad de México`
6. Categoría del sector: `Salud`
7. Tamaño del negocio: `Pequeño (1-10 empleados)`
8. Clic en **"Crear"**
9. En **"Flujos de datos"** → **"Web"**:
   - URL: `https://dralbenrosas.com`
   - Nombre: `Sitio Dr. Alben Rosas`
10. Clic en **"Crear flujo"**
11. **Copia el "ID de medición"** — formato `G-XXXXXXXXXX` — está en la esquina superior derecha del flujo

**Tiempo estimado: 8 minutos**

### 🤖 Yo configuro (cuando me des el G-XXXXXXXXXX):
- Tag de GA4 Configuration en GTM (dispara en todas las páginas)
- Evento `page_view` automático
- Evento `whatsapp_click` con parámetros
- Evento `phone_click` con parámetros
- Evento `cotizador_interaccion` (quiz del sitio)
- Scroll depth tracking (25%, 50%, 75%, 90%)
- Duración de sesión como evento de engagement

---

## PASO 4 — Meta Pixel: Crear y conectar

### 👤 Tú haces:

**4.1 — Crear Business Manager (si no lo tienes aún):**
1. Ve a **business.facebook.com**
2. Clic en **"Crear cuenta"**:
   - Nombre del negocio: `Dr. Alben Rosas — Cirugía General`
   - Tu nombre: `Alben Rosas`
   - Email: `alben.rosas@gmail.com`
3. Sigue el proceso de verificación

**4.2 — Conectar tus cuentas al Business Manager:**
1. En Business Manager → **"Configuración del negocio"** (ícono de engranaje)
2. **Cuentas → Páginas → "Agregar"** → "Agregar una página" → busca tu Página de Facebook y agrégala
3. **Cuentas → Cuentas de Instagram → "Agregar"** → conecta @dralbenrosas
4. **Cuentas → Cuentas publicitarias → "Crear nueva cuenta publicitaria"**:
   - Nombre: `Nebla Ads`
   - Zona horaria: `México/Ciudad de México`
   - Moneda: `MXN`
5. En la cuenta publicitaria, agrega un **método de pago** (tarjeta de crédito/débito)

**4.3 — Crear el Pixel:**
1. En Business Manager → **"Fuentes de datos" → "Píxeles" → "Agregar"**
2. Nombre: `dralbenrosas.com`
3. URL: `https://dralbenrosas.com`
4. Clic en **"Continuar"**
5. Selecciona **"Conectar manualmente"** → **"Instalar código manualmente"**
6. **Copia el Pixel ID** — número de 15-16 dígitos que aparece en la parte superior

**4.4 — Copiar también el Business ID:**
1. En Business Manager → Configuración → **"Info del negocio"**
2. Copia el **"ID del negocio de Meta"** — número largo

**Tiempo estimado: 20-25 minutos**

### 🤖 Yo configuro (cuando me des el Pixel ID):
- Tag Meta Pixel Base (PageView en todas las páginas) en GTM
- Evento `Lead` en GTM cuando se hace clic en WhatsApp
- Evento `Contact` en GTM cuando se hace clic en teléfono
- Evento `ViewContent` con parámetro del servicio visto (vesícula/hernia/etc.)

---

## PASO 5 — Verificación de dominio en Meta

> Necesario para que Meta reconozca dralbenrosas.com como tu dominio y puedas asignar eventos de conversión correctamente.

### 👤 Tú haces:

**Opción A — DNS en GoDaddy (recomendada, más permanente):**

1. En Meta Business Manager → **"Configuración del negocio" → "Seguridad de marca" → "Dominios"**
2. Clic en **"Agregar"** → escribe `dralbenrosas.com` → clic en **"Agregar dominio"**
3. Meta te muestra un **código TXT de verificación** — cópialo (formato: `facebook-domain-verification=XXXXXXXXXX`)
4. Ve a **godaddy.com** → inicia sesión → **"Mis productos" → "DNS"** del dominio dralbenrosas.com
5. Clic en **"Agregar registro"**:
   - Tipo: `TXT`
   - Nombre: `@`
   - Valor: el código que copiaste de Meta (sin comillas)
   - TTL: `1 hora`
6. Guarda
7. Regresa a Meta → clic en **"Verificar dominio"**

> ⚠️ Los cambios DNS pueden tardar hasta 24 horas en propagarse. Es normal.

**Opción B — Meta tag en el HTML (más rápido si tienes acceso al código):**

Meta también acepta agregar un `<meta>` tag en el `<head>` del sitio. Si tienes el HTML disponible puedo generarlo para que lo subas a Netlify.

---

## PASO 6 — Google Ads: Crear cuenta y configurar conversión

### 👤 Tú haces:

**6.1 — Crear la cuenta:**
1. Ve a **ads.google.com**
2. Inicia sesión con alben.rosas@gmail.com
3. Al crear, Google te fuerza a crear una campaña — busca el enlace pequeño **"Cambiar a modo experto"** abajo de la pantalla
4. Selecciona **"Crear campaña sin objetivo"** y luego **"Búsqueda"**
5. **Muy importante:** En la pantalla de configuración, en la parte inferior busca **"Más configuraciones"** → selecciona **"Configuración de conversiones"** → puedes omitirlo por ahora
6. Dale un nombre a la campaña: `Vesícula — Búsqueda` (la configuraremos después)
7. Ponle un presupuesto temporal bajo ($50 MXN) para poder avanzar, no la activamos todavía
8. Zona horaria: `México (GMT-7)`
9. Moneda: `MXN`
10. Guarda y **anota el ID de cliente** — número formato `XXX-XXX-XXXX` en la esquina superior derecha

**6.2 — Crear la conversión de WhatsApp:**
1. Dentro de Google Ads → **Herramientas (ícono llave inglesa) → Medición → Conversiones**
2. Clic en **"+ Nueva acción de conversión"** → **"Sitio web"**
3. Categoría: `Contacto`
4. Nombre: `WhatsApp Click`
5. Valor: Sin valor asignado (o $500 MXN si quieres)
6. Recuento: `Una` conversión por clic
7. Ventana de conversión clic: `30 días`
8. Modelo de atribución: `Basado en datos` (o `Último clic` si basado en datos no está disponible)
9. Clic en **"Guardar y continuar"**
10. Selecciona **"Usar Google Tag Manager"**
11. **Copia el "ID de conversión"** (formato `AW-XXXXXXXXX`) y la **"Etiqueta de conversión"**

**Tiempo estimado: 15 minutos**

### 🤖 Yo configuro (cuando me des AW-XXXXXXXXX y la etiqueta):
- Tag Google Ads Conversion en GTM ligado al activador de clic en WhatsApp
- Tag Google Ads Remarketing (para audiencias de remarketing futuras)

---

## PASO 7 — GTM: Configuración completa de tags y triggers

> Este paso lo hago **yo** una vez que tengas los IDs del Paso 1-6.
> A continuación detallo exactamente qué voy a configurar para que lo puedas revisar.

### 🤖 Lo que voy a crear en GTM:

**VARIABLES (necesarias para los triggers):**
```
Variable 1: Click URL — tipo: URL del clic (built-in)
Variable 2: Click Text — tipo: Texto del clic (built-in)
Variable 3: Page URL — tipo: URL de la página (built-in)
Variable 4: Scroll Depth — tipo: porcentaje de scroll (built-in)
```

**ACTIVADORES (triggers):**
```
Trigger 1: All Pages
  Tipo: Page View
  Condición: Todas las páginas

Trigger 2: WhatsApp Click
  Tipo: Clic — Solo enlaces
  Condición: Click URL contiene "wa.me" O contiene "526634370584"

Trigger 3: Phone Click
  Tipo: Clic — Solo enlaces
  Condición: Click URL contiene "526121467076" O contiene "tel:"

Trigger 4: Cotizador Interacción
  Tipo: Clic — Todos los elementos
  Condición: Click classes contiene "cotizador" O Click element matches CSS selector [data-cotizador]
  (ajustar según estructura HTML real del quiz)

Trigger 5: Scroll 75%
  Tipo: Profundidad de desplazamiento
  Profundidades: 75
  Condición: Todas las páginas
```

**TAGS:**
```
Tag 1: GA4 — Configuración
  Tipo: Google Analytics: Configuración de GA4
  ID de medición: G-XXXXXXXXXX
  Activador: All Pages

Tag 2: GA4 — WhatsApp Click
  Tipo: Evento de GA4
  ID de medición: G-XXXXXXXXXX
  Nombre del evento: whatsapp_click
  Parámetros: link_url = {{Click URL}}
  Activador: WhatsApp Click

Tag 3: GA4 — Phone Click
  Tipo: Evento de GA4
  Nombre del evento: phone_click
  Parámetros: phone_number = {{Click URL}}
  Activador: Phone Click

Tag 4: GA4 — Scroll 75%
  Tipo: Evento de GA4
  Nombre del evento: scroll_depth
  Parámetros: depth = 75
  Activador: Scroll 75%

Tag 5: Meta Pixel — Base (PageView)
  Tipo: HTML personalizado
  Código: Pixel base con fbq('init', 'PIXEL_ID') + fbq('track', 'PageView')
  Activador: All Pages

Tag 6: Meta Pixel — Lead (WhatsApp)
  Tipo: HTML personalizado
  Código: fbq('track', 'Lead', {content_name: 'WhatsApp Click'})
  Activador: WhatsApp Click

Tag 7: Meta Pixel — Contact (Teléfono)
  Tipo: HTML personalizado
  Código: fbq('track', 'Contact')
  Activador: Phone Click

Tag 8: Google Ads — Conversión WhatsApp
  Tipo: Conversión de Google Ads
  ID de conversión: AW-XXXXXXXXX
  Etiqueta: XXXXXXXXXXXX
  Activador: WhatsApp Click

Tag 9: Google Ads — Remarketing
  Tipo: Google Ads Remarketing
  ID de conversión: AW-XXXXXXXXX
  Activador: All Pages
```

**Resultado:** Toda la medición cubierta. Una vez publicado el contenedor, los datos fluyen a GA4, Meta Pixel y Google Ads simultáneamente.

---

## PASO 8 — SEO básico

> El SEO básico ya está parcialmente en el sitio por su buena estructura. Estas son las mejoras adicionales.

### 👤 Tú verificas / me das acceso:

1. **Google Search Console:**
   - Ve a **search.google.com/search-console**
   - Agrega propiedad: `https://dralbenrosas.com`
   - Método de verificación: **"Google Analytics"** (si GA4 ya está instalado, se verifica automáticamente)
   - O método **"DNS"** → agrega un registro TXT en GoDaddy (igual que Meta, pero con el código de Google)

2. **Google Business Profile:**
   - Ve a **business.google.com**
   - Crea perfil:
     - Nombre: `Dr. Alben Rosas — Cirujano General`
     - Categoría: `Cirujano`
     - Dirección: Médica del Cortés, Blvd. Pino Pallas 104, Villas del Encanto, La Paz, BCS
     - Teléfono: +52 612 146 7076
     - Sitio web: https://dralbenrosas.com
     - Horario: Lunes–Viernes
   - Verificación: Google envía tarjeta postal o te llama al teléfono del negocio

### 🤖 Lo que agrego al HTML del sitio (si me das el código fuente o acceso):

**Schema markup LocalBusiness + Physician** (mejora aparecer en búsquedas locales y en Google Knowledge Panel):

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["Physician", "LocalBusiness"],
  "name": "Dr. Alben Eduardo Rosas Ojeda",
  "alternateName": "Dr. Alben Rosas — Cirujano General",
  "description": "Cirujano general en La Paz, BCS. Especialista en vesícula, hernias y cirugía gastrointestinal. Cirugía laparoscópica, paquete todo incluido.",
  "url": "https://dralbenrosas.com",
  "telephone": "+526121467076",
  "image": "https://dralbenrosas.com/og-image.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Blvd. Pino Pallas 104",
    "addressLocality": "La Paz",
    "addressRegion": "Baja California Sur",
    "postalCode": "23085",
    "addressCountry": "MX"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 24.1426,
    "longitude": -110.3128
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "09:00",
      "closes": "18:00"
    }
  ],
  "medicalSpecialty": "Surgery",
  "availableService": [
    {"@type": "MedicalProcedure", "name": "Colecistectomía laparoscópica"},
    {"@type": "MedicalProcedure", "name": "Cirugía de hernia inguinal"},
    {"@type": "MedicalProcedure", "name": "Cirugía de hernia umbilical"},
    {"@type": "MedicalProcedure", "name": "Apendicectomía"}
  ],
  "sameAs": [
    "https://www.instagram.com/dralbenrosas",
    "https://www.facebook.com/share/1CyaYtTUFa/"
  ]
}
</script>
```

**Meta tags de Open Graph** (para que cuando compartas el link en WhatsApp/redes se vea bien):

```html
<meta property="og:title" content="Dr. Alben Rosas — Cirujano General en La Paz, BCS">
<meta property="og:description" content="Especialista en vesícula, hernias y cirugía digestiva. Cirugía laparoscópica en 7-14 días, paquete todo incluido. La Paz, BCS.">
<meta property="og:url" content="https://dralbenrosas.com">
<meta property="og:type" content="website">
<meta property="og:image" content="https://dralbenrosas.com/og-image.jpg">
<meta property="og:locale" content="es_MX">
<meta name="twitter:card" content="summary_large_image">
```

> Para el `og:image` necesitas una imagen de 1200×630 px. Puede ser una foto del Dr. o el logo sobre fondo Crema.

---

## PASO 9 — Rendimiento y velocidad

### 👤 Tú ejecutas estas pruebas:

1. Ve a **pagespeed.web.dev** → escribe `https://dralbenrosas.com` → clic en "Analizar"
2. Compárteme los puntajes de Mobile y Desktop
3. Ve a **gtmetrix.com** → registra cuenta gratis → analiza `dralbenrosas.com`

**Puntajes objetivo:**
| Métrica | Mínimo aceptable | Objetivo |
|---------|-----------------|---------|
| PageSpeed Mobile | >70 | >85 |
| PageSpeed Desktop | >85 | >95 |
| LCP (Largest Contentful Paint) | <3.5s | <2.5s |
| CLS (Cumulative Layout Shift) | <0.15 | <0.1 |

Con los resultados yo te digo qué optimizar específicamente.

### Optimizaciones comunes en Netlify (sin tocar código):
- Netlify ya incluye CDN automático ✅
- Netlify ya comprime con Gzip/Brotli automáticamente ✅
- Verificar que el dominio tenga HTTPS activo: **Site configuration → Domain management → HTTPS** → debe decir "Certificate provisioned" ✅

---

## PASO 10 — Preparación para campañas

> Una vez instalado todo el tracking, el sitio está listo para recibir tráfico pagado.

### Google Ads — Verificación previa al lanzamiento:
- [ ] Tag Assistant confirma que GTM dispara en dralbenrosas.com
- [ ] GA4 muestra datos en tiempo real cuando visitas el sitio
- [ ] El evento `whatsapp_click` aparece en GA4 Tiempo real cuando haces clic en el botón de WhatsApp
- [ ] Conversión de Google Ads aparece como "Activa" en Herramientas → Conversiones
- [ ] Google Business Profile verificado y publicado

### Meta Ads — Verificación previa al lanzamiento:
- [ ] Pixel ID aparece "Activo" en Meta Business Manager → Píxeles
- [ ] Evento PageView se registra cuando visitas dralbenrosas.com
- [ ] Evento Lead se registra cuando haces clic en WhatsApp
- [ ] Dominio dralbenrosas.com aparece como "Verificado" en Seguridad de marca → Dominios
- [ ] Instagram @dralbenrosas conectado al Business Manager
- [ ] Página de Facebook conectada al Business Manager
- [ ] Método de pago activo en la cuenta publicitaria

### UTMs para todas las campañas:
```
Google Ads:
https://dralbenrosas.com/?utm_source=google&utm_medium=cpc&utm_campaign={campaign}&utm_term={keyword}

Meta — Vesícula:
https://dralbenrosas.com/?utm_source=meta&utm_medium=paid_social&utm_campaign=vesicula_mes1

Meta — Hernias:
https://dralbenrosas.com/?utm_source=meta&utm_medium=paid_social&utm_campaign=hernias_mes1

Meta — Remarketing:
https://dralbenrosas.com/?utm_source=meta&utm_medium=remarketing&utm_campaign=retargeting
```

---

## RESUMEN DE ACCIONES

### 👤 Lo que tú haces (en orden):

| # | Tarea | Plataforma | Tiempo |
|---|-------|-----------|--------|
| 1 | Crear cuenta GTM + copiar Container ID | tagmanager.google.com | 5 min |
| 2 | Instalar GTM en Netlify (Snippet Injection) | app.netlify.com | 5 min |
| 3 | Crear propiedad GA4 + copiar Measurement ID | analytics.google.com | 8 min |
| 4 | Crear Meta Business Manager | business.facebook.com | 10 min |
| 5 | Conectar Instagram + Facebook Page al BM | business.facebook.com | 10 min |
| 6 | Crear Pixel + copiar Pixel ID | business.facebook.com | 5 min |
| 7 | Copiar Business ID | business.facebook.com | 2 min |
| 8 | Verificar dominio en Meta (DNS en GoDaddy) | godaddy.com | 10 min |
| 9 | Crear cuenta Google Ads + conversión WhatsApp + copiar IDs | ads.google.com | 15 min |
| 10 | Crear Google Business Profile | business.google.com | 15 min |
| 11 | Verificar sitio en Google Search Console | search.google.com/search-console | 5 min |
| 12 | Correr PageSpeed test + compartir resultados | pagespeed.web.dev | 3 min |
| **Total** | | | **~93 min** |

### 🤖 Lo que yo hago (cuando me des los IDs):

| # | Tarea |
|---|-------|
| 1 | Configurar todos los tags en GTM (GA4, Pixel, Google Ads, conversiones) |
| 2 | Publicar el contenedor GTM |
| 3 | Verificar que todos los eventos disparan correctamente |
| 4 | Agregar Schema markup al HTML del sitio |
| 5 | Agregar Open Graph meta tags |
| 6 | Actualizar tracking-setup.md con los IDs reales |
| 7 | Crear la estructura de campañas Google Ads para importar |
| 8 | Crear las campañas de Meta Ads con toda la segmentación |

---

## FORMULARIO PARA DARME LOS IDs

Cuando termines, comparte esto conmigo:

```
GTM Container ID:     GTM-PXWFLFT5     ✅
GA4 Measurement ID:   G-3Q0C76JXB3     ✅
Meta Pixel ID:        3456701621158975  ✅
Meta Business ID:     2482834265523958  ✅
Google Ads Conversion ID:    AW-         (pendiente)
Google Ads Conversion Label:             (pendiente)
```

Con esos 6 datos configuro todo en menos de 30 minutos.

---

*Última actualización: 2026-05-25 | Próxima acción: Agregar Meta Pixel en GTM + verificación de dominio*
