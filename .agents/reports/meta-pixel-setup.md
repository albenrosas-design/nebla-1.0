# Meta Pixel Setup — dralbenrosas.com
*Pixel ID: `3456701621158975` | GTM: GTM-PXWFLFT5 | Fecha: 2026-05-25*

---

## PASO 1 — Agregar Meta Pixel en GTM

No importas JSON esta vez. Agregas 2 tags directamente en GTM.

### Tag 1: Meta Pixel — PageView (base)

1. Ve a **tagmanager.google.com** → entra a `GTM-PXWFLFT5`
2. Menú izquierdo → **"Etiquetas"** → clic en **"Nueva"**
3. Clic en el área de **"Configuración de la etiqueta"** → selecciona **"HTML personalizado"**
4. Pega este código exactamente:

```html
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
```

5. Marca la casilla **"Admitir document.write"** → déjala **desmarcada** (NO marcar)
6. Clic en el área de **"Activación"** → selecciona **"All Pages"** (el trigger que ya existe)
7. Nombre de la etiqueta: `Meta Pixel — PageView`
8. Clic en **"Guardar"**

---

### Tag 2: Meta Pixel — Lead (WhatsApp Click)

Este tag se dispara cada vez que alguien hace clic en el botón de WhatsApp — registra una conversión Lead en Meta.

1. Etiquetas → **"Nueva"**
2. Tipo: **"HTML personalizado"**
3. Pega este código:

```html
<script>
  fbq('track', 'Lead');
</script>
```

4. Activador → selecciona **"Clic WhatsApp"** (el trigger que importaste antes — busca ese nombre)
5. Nombre: `Meta Pixel — Lead (WhatsApp)`
6. **"Guardar"**

---

### Publicar los 2 tags nuevos

1. Clic en el botón rojo **"Enviar"** (esquina superior derecha)
2. Nombre de versión: `v2 — Meta Pixel + Lead WhatsApp`
3. Descripción: `Pixel de Meta agregado: PageView en todas las páginas, Lead en clic WhatsApp`
4. Clic en **"Publicar"**

---

## PASO 2 — Verificar que el Pixel está recibiendo datos

### Opción A — Meta Pixel Helper (Chrome Extension)

1. Instala la extensión **"Meta Pixel Helper"** en Chrome
2. Visita **dralbenrosas.com**
3. La extensión debe mostrar en verde: **Pixel 3456701621158975 — PageView ✅**
4. Haz clic en el botón de WhatsApp → debe aparecer **Lead ✅**

### Opción B — Events Manager en Meta

1. Ve a **business.facebook.com** → Fuentes de datos → Píxeles → `3456701621158975`
2. Clic en **"Ver actividad"** o tab **"Eventos"**
3. Visita tu sitio en otra pestaña y haz clic en WhatsApp
4. En 30-60 segundos deberías ver `PageView` y `Lead` aparecer en tiempo real

---

## PASO 3 — Verificar dominio en Meta (OBLIGATORIO para conversiones)

Meta requiere verificar que eres dueño del dominio antes de optimizar campañas para conversiones.

### 3.1 — Obtener el código de verificación

**Código confirmado:** `facebook-domain-verification=y9rtbme5cmct99lxmwtgrpc8p7gkm8`

### 3.2 — Agregar el TXT record en GoDaddy

1. Ve a **godaddy.com** → inicia sesión
2. Menú superior → **"Mis productos"** → busca `dralbenrosas.com` → clic en **"DNS"**
3. Clic en **"Agregar registro"** (o "Add Record")
4. Selecciona tipo: **TXT**
5. Llena los campos:
   - **Host/Nombre**: `@`
   - **Valor/Value**: `facebook-domain-verification=y9rtbme5cmct99lxmwtgrpc8p7gkm8`
   - **TTL**: 1 hora (600 segundos)
6. Clic en **"Guardar"**

### 3.3 — Verificar en Meta

1. Regresa a Meta Business Manager → Dominios
2. Clic en **"Verificar dominio"**
3. Si los DNS ya se propagaron (puede tardar 5-30 minutos), aparecerá **"Verificado ✅"**

> Si no verifica de inmediato, espera 30 minutos e intenta de nuevo. Los cambios de DNS tardan en propagarse.

---

## PASO 4 — Marcar Lead (WhatsApp) como conversión principal en Meta

1. En Meta Business Manager → Fuentes de datos → Píxeles → `3456701621158975`
2. Clic en tab **"Eventos de conversión"** (o "Aggregated Event Measurement")
3. Clic en **"Configurar eventos web"**
4. Busca el evento **`Lead`** → actívalo como evento de conversión
5. Asigna prioridad **1** (la más alta — es tu conversión principal)
6. Guarda

---

## PASO 5 — Configurar objetivo de conversión en Meta Ads

Cuando crees tus campañas de Meta Ads:

- **Objetivo de campaña**: `Clientes potenciales` o `Conversiones`
- **Evento de conversión**: `Lead` (desde el Pixel `3456701621158975`)
- **Ubicación del evento**: Sitio web (Website)

Esto permite que Meta Ads optimice para mostrar tus anuncios a personas que tienen mayor probabilidad de hacer clic en WhatsApp.

---

## RESUMEN — Estado del tracking

| Evento | GA4 | Meta Pixel | Google Ads |
|--------|-----|-----------|-----------|
| `page_view` / `PageView` | ✅ GTM publicado | 🔄 Agregar Tag 1 | — |
| `whatsapp_click` / `Lead` | ✅ GTM publicado | 🔄 Agregar Tag 2 | ⏳ Pendiente AW- ID |
| `phone_click` | ✅ GTM publicado | — | — |
| `scroll_depth` | ✅ GTM publicado | — | — |

---

## DATOS CONFIRMADOS

| Campo | Valor |
|-------|-------|
| Meta Pixel ID | `3456701621158975` |
| Meta Business ID | `2482834265523958` |
| Dominio a verificar | `dralbenrosas.com` |
| Evento de conversión principal | `Lead` (WhatsApp click) |
| GTM Container | `GTM-PXWFLFT5` |

---

*Próximo paso: Google Ads Conversion Tag (requiere AW-XXXXXXXXX + Label)*
