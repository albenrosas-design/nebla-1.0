# GTM Setup & Verificación de Eventos
*GTM: GTM-PXWFLFT5 | GA4: G-3Q0C76JXB3 | Sitio: dralbenrosas.com*

---

## LO QUE YA ESTÁ CONFIGURADO

| ID | Valor |
|----|-------|
| GTM Container ID | `GTM-PXWFLFT5` |
| GA4 Measurement ID | `G-3Q0C76JXB3` |
| GTM instalado en Netlify | ✅ (Snippet Injection) |

---

## PASO 1 — Importar el contenedor GTM

El archivo `gtm-container-nebla.json` ya está configurado con:
- ✅ Google Tag GA4 (G-3Q0C76JXB3) — dispara en todas las páginas
- ✅ Evento `whatsapp_click` — dispara cuando clic en botón WhatsApp (wa.me)
- ✅ Evento `phone_click` — dispara cuando clic en teléfono (tel:)
- ✅ Evento `scroll_depth` — dispara al scrollear 75% de la página
- ✅ Variables built-in habilitadas: Click URL, Click Classes, Scroll Depth Threshold

### 👤 Tú haces:

1. Ve a **tagmanager.google.com** → entra a tu contenedor `GTM-PXWFLFT5`
2. En el menú superior, clic en el ícono de **"Admin"** (engranaje)
3. En la columna "Contenedor", clic en **"Importar contenedor"**
4. Clic en **"Elegir archivo de contenedor"** → sube el archivo `gtm-container-nebla.json`
5. En "Elegir espacio de trabajo": selecciona **"Espacio de trabajo existente"** → **"Default Workspace"**
6. En "Elegir una opción de importación": selecciona **"Combinar"** → **"Renombrar las etiquetas, los activadores y las variables en conflicto"**
7. Clic en **"Confirmar"**

Deberías ver aparecer:
- 4 etiquetas (tags)
- 4 activadores (triggers)
- 13 variables integradas (built-in)

---

## PASO 2 — Verificar en modo Vista previa (Preview)

Antes de publicar, verificamos que todo funciona.

### 👤 Tú haces:

1. En GTM → clic en el botón azul **"Vista previa"** (Preview) en la esquina superior derecha
2. Escribe `https://dralbenrosas.com` → clic en **"Connect"**
3. Se abre tu sitio en una nueva pestaña con el panel de Tag Assistant en la parte inferior

### ✅ Prueba 1 — Page View (GA4 base)

En Tag Assistant, en la sección izquierda busca el evento **"Container Loaded"** o **"Window Loaded"**.

Deberías ver:
- **"Google Tag — GA4 (G-3Q0C76JXB3)"** → marcado como ✅ **Fired** (disparó)

Si no aparece → el GTM Snippet Injection en Netlify no está activo. Vuelve a Netlify y verifica los snippets.

---

### ✅ Prueba 2 — WhatsApp Click

1. En el sitio abierto con Tag Assistant, haz clic en el botón verde **"Agendar por WhatsApp"**
2. (Puedes cerrar la ventana de WhatsApp que se abra — lo que importa es el clic)
3. Regresa a Tag Assistant

Deberías ver un nuevo evento en la lista izquierda: **"Link Click"**

Al seleccionarlo, en el panel de Tags deberías ver:
- **"GA4 — Event: whatsapp_click"** → ✅ **Fired**

Si no aparece → el botón de WhatsApp puede no tener `href="https://wa.me/..."` directo. Verificar en el HTML del sitio.

---

### ✅ Prueba 3 — Phone Click

1. Haz clic en el botón **"Llamar al consultorio"** (o el teléfono en la sección de contacto)
2. En Tag Assistant debe aparecer otro evento "Link Click"
3. Deberías ver:
- **"GA4 — Event: phone_click"** → ✅ **Fired**

---

### ✅ Prueba 4 — Scroll Depth

1. Scrollea la página hasta el final (hasta el footer)
2. En Tag Assistant deberías ver eventos "Scroll Depth"
3. Al llegar al 75% de la página:
- **"GA4 — Event: scroll_depth_75"** → ✅ **Fired**

---

## PASO 3 — Publicar el contenedor

Si todas las pruebas pasaron:

### 👤 Tú haces:

1. Cierra la vista previa (clic en **"X"** en Tag Assistant o en **"Salir de la vista previa"** en GTM)
2. En GTM, clic en el botón rojo **"Enviar"** (Submit) — esquina superior derecha
3. En "Versión":
   - Nombre de la versión: `v1 — GA4 + WhatsApp + Phone + Scroll`
   - Descripción: `Configuración inicial: GA4, eventos de conversión WhatsApp y teléfono, scroll depth`
4. Clic en **"Publicar"**

✅ **El contenedor está activo.** Todos los eventos empiezan a registrarse en GA4.

---

## PASO 4 — Verificar en GA4 en tiempo real

### 👤 Tú haces:

1. Ve a **analytics.google.com** → selecciona la propiedad `dralbenrosas.com`
2. En el menú izquierdo → **"Informes"** → **"Tiempo real"**
3. Abre otra pestaña y visita **dralbenrosas.com**

Deberías ver en GA4 Tiempo real:
- Un usuario activo en el sitio
- Evento: `page_view`

4. Haz clic en el botón de WhatsApp en el sitio
5. En GA4 Tiempo real → sección **"Recuento de eventos por nombre de evento"**:
   - Deberías ver `whatsapp_click` aparecer

6. Haz clic en el teléfono del consultorio:
   - Deberías ver `phone_click` aparecer

Si ves los eventos en GA4 Tiempo real → **🎉 El tracking está funcionando correctamente.**

---

## PASO 5 — Configurar conversiones en GA4

Para que GA4 trate `whatsapp_click` como conversión principal:

### 👤 Tú haces:

1. En GA4 → **Admin** (engranaje abajo a la izquierda) → **"Eventos"**
2. Busca `whatsapp_click` en la lista de eventos
3. Activa el toggle **"Marcar como conversión"** → debe quedar en azul ✅
4. Haz lo mismo para `phone_click`

Ahora estos eventos aparecen en **Informes → Conversiones** de GA4.

---

## RESUMEN DE EVENTOS CONFIGURADOS

| Evento GA4 | Cuándo dispara | Conversión |
|------------|---------------|-----------|
| `page_view` | Cada visita al sitio | No |
| `whatsapp_click` | Clic en botón WhatsApp (wa.me) | ✅ Sí |
| `phone_click` | Clic en teléfono (tel:) | ✅ Sí |
| `scroll_depth` | Usuario scrollea 75% de la página | No (engagement) |

---

## PRÓXIMOS PASOS (cuando tengas los IDs restantes)

| Siguiente configuración | Requiere |
|------------------------|---------|
| Meta Pixel | Pixel ID de Meta Business Manager |
| Google Ads Conversion | Cuenta Google Ads creada + Conversion ID |
| Verificación de dominio Meta | Business ID + acceso a GoDaddy DNS |
| Schema markup SEO | Acceso al HTML fuente del sitio |

---

## SOLUCIÓN DE PROBLEMAS COMUNES

### GTM no aparece en Tag Assistant
→ Los snippets de Netlify no están guardados correctamente.
→ Ve a Netlify → Site configuration → Build & deploy → Post processing → Snippet injection → verifica que existen los 2 snippets con `GTM-PXWFLFT5`.

### WhatsApp Click no dispara
→ El botón WhatsApp en el sitio puede usar un evento JavaScript en lugar de un `href="https://wa.me/..."` directo.
→ Solución: usar también el trigger tipo "Todos los elementos" con condición Click Text contiene "WhatsApp".

### GA4 no muestra datos en tiempo real
→ Espera 30 segundos después de cargar el sitio. GA4 Tiempo real tiene un pequeño delay.
→ Verifica que el Measurement ID en GTM sea exactamente `G-3Q0C76JXB3`.

### Evento scroll_depth no dispara
→ Verifica que las variables built-in están habilitadas: en GTM → Variables → Built-in Variables → debe aparecer "Scroll Depth Threshold" y "Scroll Depth Units".
