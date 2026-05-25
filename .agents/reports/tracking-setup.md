# Tracking Setup — dralbenrosas.com
*Sitio: Custom | Plataforma: HTML propio | CTA principal: WhatsApp*

> **Estrategia:** Instalar Google Tag Manager (GTM) una sola vez en el sitio. Todo el tracking futuro (GA4, Meta Pixel, Google Ads, conversiones) se configura desde GTM sin volver a tocar el código.

---

## PASO 1 — Crear cuenta de Google Tag Manager

1. Ve a **tagmanager.google.com**
2. Inicia sesión con alben.rosas@gmail.com
3. Crear cuenta:
   - Nombre de cuenta: `Nebla`
   - País: México
4. Crear contenedor:
   - Nombre: `dralbenrosas.com`
   - Plataforma: **Web**
5. Acepta los términos → GTM te muestra **2 snippets de código**

Guarda los dos snippets — los vas a necesitar en el Paso 2.

Tu Container ID tendrá este formato: `GTM-XXXXXXX`

---

## PASO 2 — Instalar GTM en el sitio (1 sola vez)

Dile a tu desarrollador que agregue estos dos bloques al HTML de **todas las páginas** del sitio:

### Snippet 1 — En el `<head>` (lo más arriba posible)

```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
<!-- End Google Tag Manager -->
```

> ⚠️ Reemplazar `GTM-XXXXXXX` con tu Container ID real.

### Snippet 2 — Justo después de la etiqueta `<body>` (primera línea del body)

```html
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```

> ⚠️ Reemplazar `GTM-XXXXXXX` con tu Container ID real.

**Eso es todo lo que el desarrollador necesita hacer.** El resto se configura desde GTM.

---

## PASO 3 — Crear propiedad GA4

1. Ve a **analytics.google.com**
2. Inicia sesión con alben.rosas@gmail.com
3. Crear propiedad:
   - Nombre: `dralbenrosas.com`
   - País: México
   - Moneda: MXN
   - Industria: Salud
4. En "Flujo de datos web":
   - URL: `https://dralbenrosas.com`
   - Nombre: `Sitio web Dr. Alben Rosas`
5. Copia tu **ID de medición** → formato: `G-XXXXXXXXXX`

---

## PASO 4 — Configurar GA4 en GTM

En GTM → **Etiquetas → Nueva etiqueta:**

```
Nombre: GA4 — Configuración
Tipo de etiqueta: Google Analytics: Evento de GA4
ID de medición: G-XXXXXXXXXX  ← tu Measurement ID
Activador: Todas las páginas (All Pages)
```

Publicar el contenedor después de agregar esta etiqueta.

---

## PASO 5 — Crear Meta Pixel

> Requiere tener Meta Business Manager ya creado (ver ads-launch-phase0.md Parte 2, paso 2.1)

1. En **Meta Business Manager → Fuentes de datos → Píxeles**
2. Crear Pixel:
   - Nombre: `Nebla — dralbenrosas.com`
3. **Pixel ID: `3456701621158975`** ✅ (confirmado 2026-05-25)

---

## PASO 6 — Configurar Meta Pixel en GTM

En GTM → **Etiquetas → Nueva etiqueta:**

### Tag 1: Meta Pixel — PageView (base)

```
Nombre: Meta Pixel — PageView
Tipo: HTML personalizado
HTML:
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '3456701621158975');
fbq('track', 'PageView');
</script>

Activador: Todas las páginas (All Pages)
```

---

## PASO 7 — Configurar conversión: WhatsApp Click

Esta es la conversión más importante. Se dispara cuando alguien hace clic en el botón de WhatsApp. Se registra como conversión tanto en Meta como en Google Ads.

### 7.1 — Crear activador de clic en WhatsApp (GTM)

En GTM → **Activadores → Nuevo activador:**

```
Nombre: Clic WhatsApp
Tipo de activador: Clic — Solo enlaces
Activar cuando: URL del clic contiene "wa.me"  O  URL del clic contiene "526634370584"
```

> El número de WhatsApp del sitio es +52 663 437 0584 → wa.me/526634370584
> El teléfono del consultorio (+52 612 146 7076) es diferente — crear activador separado si quieres trackearlo también.

### 7.2 — Tag: Meta Pixel Lead (WhatsApp click)

En GTM → **Etiquetas → Nueva etiqueta:**

```
Nombre: Meta Pixel — Lead (WhatsApp)
Tipo: HTML personalizado
HTML:
<script>
  fbq('track', 'Lead');
</script>
Activador: Clic WhatsApp  ← el activador creado arriba
```

### 7.3 — Tag: GA4 Event — whatsapp_click

```
Nombre: GA4 — whatsapp_click
Tipo: Evento de GA4
ID de medición: G-XXXXXXXXXX
Nombre del evento: whatsapp_click
Activador: Clic WhatsApp
```

### 7.4 — Tag: Google Ads Conversion (configurar después de crear cuenta)

Una vez que tengas tu cuenta de Google Ads y el ID de conversión:

```
Nombre: Google Ads — Conversión WhatsApp
Tipo: Conversión de Google Ads
ID de conversión: AW-XXXXXXXXX    ← de Google Ads
Etiqueta de conversión: XXXXXXXXXXX  ← de Google Ads
Activador: Clic WhatsApp
```

---

## PASO 8 — Publicar GTM y verificar

1. En GTM → **Enviar** → Publicar
2. Instala la extensión **"Tag Assistant"** de Google Chrome
3. Visita dralbenrosas.com con Tag Assistant activo
4. Verifica que aparezcan: GTM, GA4, Meta Pixel
5. Haz clic en el botón de WhatsApp → verifica que dispare el evento Lead en Meta y `whatsapp_click` en GA4

**En Meta:** Ve a Business Manager → Píxeles → Ver actividad → debe aparecer "Lead" cuando haces clic en WhatsApp

**En GA4:** Ve a Analytics → Informes → Tiempo real → debe aparecer `whatsapp_click` como evento activo

---

## PASO 9 — Configurar conversión en Google Ads

1. En Google Ads → **Herramientas → Medición → Conversiones → Nueva conversión**
2. Tipo: **Sitio web**
3. Nombre: `WhatsApp Click`
4. Categoría: `Contacto`
5. Valor: Sin valor (o $500 MXN si quieres asignar valor por lead)
6. Recuento: `Una` (una conversión por sesión)
7. Ventana de conversión: 30 días
8. Atribución: Basada en datos (o Último clic al inicio)
9. GTM te dará el **ID de conversión** y **Etiqueta de conversión** para el Paso 7.4

---

## PASO 10 — Configurar CAPI de Meta (opcional, pero recomendado)

> La Conversions API (CAPI) envía eventos desde el servidor, complementando el pixel del navegador. Mejora el match de audiencias y reduce pérdida de datos por bloqueadores de anuncios.

Para una implementación simple sin sitio complejo, usar **CAPI Gateway** de Meta:
1. En Meta Business Manager → Fuentes de datos → Píxeles → Tu Pixel → Configuración
2. Busca "Conversions API" → "Instalar con socios" → "CAPI Gateway"
3. Sigue el wizard — no requiere código

---

## RESUMEN — Orden de instalación

```
Semana actual:
  1. [ ] Crear cuenta GTM → obtener GTM-XXXXXXX
  2. [ ] Desarrollador instala GTM en <head> y <body> del sitio
  3. [ ] Crear propiedad GA4 → obtener G-XXXXXXXXXX
  4. [ ] Crear Meta Business Manager + Pixel → obtener Pixel ID
  5. [ ] Crear cuenta Google Ads

  En GTM (tú lo configuras):
  6. [ ] Agregar tag GA4 Configuration
  7. [ ] Agregar tag Meta Pixel PageView
  8. [ ] Crear activador "Clic WhatsApp"
  9. [ ] Agregar tags de conversión WhatsApp (Meta Lead + GA4 event)
  10. [ ] Publicar contenedor GTM
  11. [ ] Verificar con Tag Assistant

  Cuando Google Ads esté creado:
  12. [ ] Configurar conversión en Google Ads
  13. [ ] Agregar tag Google Ads Conversion en GTM
  14. [ ] Republicar GTM

  Campaña puede lanzar:
  15. [ ] Subir estructura de campañas Google Ads (ver ads-launch-phase0.md)
  16. [ ] Subir campañas Meta Ads con destino al sitio web
  17. [ ] Activar campañas
```

---

## CONFIGURACIÓN DE UTMs (para todas las campañas)

Todos los links de anuncios deben llevar UTMs para que GA4 atribuya correctamente:

### Google Ads — usar en URL final de cada anuncio:
```
https://dralbenrosas.com/?utm_source=google&utm_medium=cpc&utm_campaign={campaign}&utm_content={adgroup}&utm_term={keyword}
```
> Las llaves `{campaign}` etc. son variables dinámicas de Google — no las cambies.

### Meta Ads — usar en URL del anuncio:
```
https://dralbenrosas.com/?utm_source=meta&utm_medium=paid_social&utm_campaign=vesicula_mes1
https://dralbenrosas.com/?utm_source=meta&utm_medium=paid_social&utm_campaign=hernias_mes1
```

---

## EVENTOS A TRACKEAR (prioridad)

| Evento | Plataforma | Qué es |
|--------|-----------|--------|
| `whatsapp_click` | GA4 + Google Ads + Meta (Lead) | Clic en botón WhatsApp +52 663 437 0584 → conversión principal |
| `phone_click` | GA4 | Clic en teléfono consultorio +52 612 146 7076 |
| `cotizador_start` | GA4 | Usuario interactuó con el quiz "Arma tu valoración en 3 toques" |
| `cotizador_complete` | GA4 + Meta (Lead) | Usuario completó el quiz → micro-conversión importante |
| `page_view` | GA4 + Meta (PageView) | Visita a cualquier página |
| `scroll_depth_75` | GA4 | Usuario scrolleó 75% de la página |

> **El cotizador ("Arma tu valoración en 3 toques")** es una micro-conversión clave: quien lo completa tiene alta intención. Crear audiencia de remarketing Meta con visitantes que completaron el quiz pero no hicieron clic en WhatsApp.

Los eventos de scroll se pueden configurar en GTM sin código usando activadores built-in.

---

*Una vez instalado el tracking, actualizar este archivo con los IDs reales obtenidos.*
