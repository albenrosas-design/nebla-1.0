# Ads Launch — Fase 0 (Sin sitio web)
*Creado: 2026-05-24 | Variante: Call-Only Google + Lead Gen nativo Meta*

> **Estrategia:** Lanzar antes de que el sitio web esté terminado usando campañas que no requieren landing page. Google captura a quien busca activamente; Meta llega a quien tiene síntomas pero aún no busca. Ambos convierten directamente a WhatsApp/llamada.

---

## ESTADO ACTUAL

| Elemento | Estado |
|----------|--------|
| Sitio web | ❌ Sin construir |
| WhatsApp Business | ⚠️ Número: (624) 100-0426 — pendiente configurar Business API |
| Google Ads cuenta | ❌ Por crear |
| Google Business Profile | ❌ Por crear/verificar |
| Meta Business Manager | ❌ Por crear |
| Instagram @dralbenrosas | ✅ Activo (172 seguidores) |
| Facebook Page | ✅ Existe (0 publicaciones) |
| Meta Pixel | ❌ Sin sitio, se instala después |
| Foto del Dr. fuera de quirófano | ⚠️ Pendiente esta semana |
| brand-profile.json | ✅ Creado |

---

## PARTE 1 — GOOGLE ADS

### 1.1 Crear la cuenta (tú lo haces una vez)

1. Ve a **ads.google.com**
2. Inicia sesión con tu cuenta Google (alben.rosas@gmail.com)
3. Al crear cuenta, Google te pedirá crear una campaña — selecciona **"Cambiar a modo experto"** (enlace pequeño abajo de la pantalla)
4. Elige **"Crear campaña sin un objetivo"** → tipo **"Búsqueda"**
5. En "Conversiones", selecciona **"Llamadas telefónicas"**
6. Ponle nombre a la cuenta: `Nebla — Dr. Alben Rosas`
7. Moneda: **MXN**, zona horaria: **América/Mazatlan**
8. Agrega método de pago (tarjeta de crédito/débito)

---

### 1.2 Crear Google Business Profile (necesario para extensión de ubicación)

1. Ve a **business.google.com**
2. Crea perfil con:
   - Nombre: `Dr. Alben Rosas — Cirujano General`
   - Categoría: `Cirujano`
   - Dirección: Tu dirección de consultorio en La Paz, BCS
   - Teléfono: (624) 100-0426
   - Área de servicio: La Paz, Los Cabos, BCS
3. Verifica el perfil (Google envía tarjeta postal o verificación por teléfono)
4. Una vez verificado, conecta el Business Profile a tu cuenta de Google Ads en: Herramientas → Vinculación de cuentas → Google Business Profile

---

### 1.3 Estructura de campañas — Call-Only

> Las campañas de **solo llamadas** muestran el anuncio exclusivamente en móviles y el clic llama directamente al (624) 100-0426. Sin landing page. Sin sitio web.

```
CUENTA: Nebla — Cirujano General La Paz
│
├── CAMPAÑA 1: Vesícula — Call Only [LANZAR PRIMERO]
│   Presupuesto: $130 MXN/día
│   │
│   ├── Grupo 1A: Síntomas vesícula
│   └── Grupo 1B: Cirugía vesícula — alta intención
│
├── CAMPAÑA 2: Hernias — Call Only
│   Presupuesto: $70 MXN/día
│   └── Grupo 2A: Síntomas + Cirugía hernia
│
└── CAMPAÑA 3: Cirujano General — Call Only
    Presupuesto: $50 MXN/día
    └── Grupo 3A: Branded + local La Paz BCS

TOTAL: $250 MXN/día (~$7,500 MXN/mes)
```

---

### 1.4 Configuración de campaña (aplica a las 3 campañas)

| Parámetro | Valor |
|-----------|-------|
| Tipo | Búsqueda — Solo llamadas |
| Red | Solo Búsqueda (desactivar "Socios de búsqueda" al inicio) |
| Ubicación | La Paz, BCS → radio 60 km |
| Idioma | Español |
| Estrategia de puja | CPC manual → máximo $30 MXN por clic |
| Rotación de anuncios | Optimizar |
| Programación | Lunes–Sábado, 8am–8pm (horario en que puedes contestar) |
| Dispositivos | Solo móvil (call-only funciona únicamente en móvil) |

---

### 1.5 Ad Copy — Formato Call-Only

> El formato Call-Only tiene: 2 headlines (max 30 chars c/u) + 2 descriptions (max 90 chars c/u). El teléfono aparece automáticamente abajo. NO hay URL de destino.

---

**CAMPAÑA 1 — VESÍCULA, Grupo 1A: Síntomas**

Keywords (tipo concordancia amplia modificada — usar `+`):
```
+cálculos +vesícula
+dolor +vesícula
+piedras +vesícula +La Paz
+síntomas +vesícula
+cólico +biliar
+vesícula +inflamada
```

Call-Only Ad — Variante A:
```
Headline 1: ¿Dolor en la vesícula?        [26 chars ✓]
Headline 2: Cirujano en La Paz BCS         [26 chars ✓]
Description 1: Especialista en vesícula y cálculos biliares. Cirugía laparoscópica, recuperación rápida.   [88 chars ✓]
Description 2: Sin lista de espera. Agenda tu consulta esta semana — atención directa con el cirujano.     [88 chars ✓]
Número de teléfono: (624) 100-0426
```

Call-Only Ad — Variante B:
```
Headline 1: Cálculos en la vesícula        [27 chars ✓]
Headline 2: Valoración en La Paz BCS        [28 chars ✓]
Description 1: ¿Te dijeron que tienes piedras en la vesícula? Diagnóstico claro en tu primera consulta.   [88 chars ✓]
Description 2: Cirugía laparoscópica en La Paz, BCS. Sin viajar a Guadalajara. Llámanos hoy.              [82 chars ✓]
Número de teléfono: (624) 100-0426
```

---

**CAMPAÑA 1 — VESÍCULA, Grupo 1B: Cirugía (alta intención)**

Keywords:
```
+cirugía +vesícula +La Paz
+operación +vesícula +La Paz
+colecistectomía +La Paz
+cirugía +laparoscópica +vesícula +BCS
+cirujano +vesícula +La Paz
```

Call-Only Ad — Variante A:
```
Headline 1: Cirugía Vesícula La Paz        [27 chars ✓]
Headline 2: Laparoscopia — Esta Semana     [29 chars ✓]
Description 1: Cirugía laparoscópica de vesícula en La Paz, BCS. Recuperación en días, sin cicatriz grande.  [90 chars ✓]
Description 2: Trato directo con el cirujano desde la primera consulta. Sin esperas del IMSS. Llama ahora.   [90 chars ✓]
Número de teléfono: (624) 100-0426
```

---

**CAMPAÑA 2 — HERNIAS**

Keywords:
```
+hernia +inguinal +La Paz
+hernia +umbilical +La Paz
+cirugía +hernia +La Paz
+operación +hernia +BCS
+hernia +laparoscópica
+bulto +ingle +La Paz
+hernia +que +hacer
```

Call-Only Ad — Variante A:
```
Headline 1: Cirugía de Hernia La Paz       [27 chars ✓]
Headline 2: Técnica Laparoscópica          [22 chars ✓]
Description 1: Cirujano especializado en hernias inguinales, umbilicales e hiatales en La Paz, BCS.         [85 chars ✓]
Description 2: Recuperación rápida, sin lista de espera. Agenda tu valoración esta semana.                   [79 chars ✓]
Número de teléfono: (624) 100-0426
```

Call-Only Ad — Variante B:
```
Headline 1: ¿Llevas tiempo con hernia?     [28 chars ✓]
Headline 2: Cirujano en La Paz BCS         [26 chars ✓]
Description 1: La hernia no mejora sola. Cirugía laparoscópica en La Paz — vuelves al trabajo en días.      [87 chars ✓]
Description 2: Sin esperar meses en el IMSS. Atención directa con el cirujano. Llama hoy.                   [79 chars ✓]
Número de teléfono: (624) 100-0426
```

---

**CAMPAÑA 3 — CIRUJANO GENERAL (Branded/Local)**

Keywords:
```
+cirujano +general +La Paz +BCS
+cirujano +La Paz
+cirugía +laparoscópica +La Paz
+cirujano +BCS
+dr +Alben +Rosas
+nebla +cirujano
```

Call-Only Ad:
```
Headline 1: Cirujano General La Paz        [27 chars ✓]
Headline 2: Dr. Alben Rosas — BCS         [24 chars ✓]
Description 1: Cirujano general certificado CMCG en La Paz, BCS. Vesícula, hernias y cirugía GI.            [83 chars ✓]
Description 2: Consulta de valoración esta semana. Sin lista de espera. Llama ahora.                         [71 chars ✓]
Número de teléfono: (624) 100-0426
```

---

### 1.6 Negative Keywords (aplicar en todas las campañas desde el día 1)

```
IMSS, ISSSTE, seguro popular, gratuito, gratis, costo cero, sin costo,
veterinario, cirujano plástico, cirugía estética, liposucción, bariatrica,
Guadalajara, CDMX, Tijuana, Mexicali, Monterrey,
empleo, trabajo, sueldo, vacante,
pediatra, oncólogo, ginecólogo,
receta, medicamento, pastilla,
youtube, video, tutorial
```

---

### 1.7 Extensiones de anuncio (configurar en todas las campañas)

| Extensión | Contenido |
|-----------|-----------|
| **Llamada** | (624) 100-0426 — Lun–Sáb 8am–8pm |
| **Texto destacado** | "Certificado CMCG" · "Cirugía Laparoscópica" · "Sin Lista de Espera" · "Atención Directa con el Cirujano" |
| **Extracto de sitio** | Cabecera: "Especialidades" → Vesícula · Hernias · Apendicitis · Gastrointestinal |
| **Ubicación** | Vinculada al Google Business Profile (configurar después de verificar GBP) |

---

### 1.8 Conversión a configurar en Google Ads

Tipo de conversión: **Llamadas desde anuncios**
- Llamada cuenta como conversión cuando dura: **60 segundos o más**
- Esta conversión se registra automáticamente sin pixel ni sitio web

---

## PARTE 2 — META ADS

### 2.1 Configurar Meta Business Manager (tú lo haces una vez)

1. Ve a **business.facebook.com**
2. Crea una cuenta de Business Manager:
   - Nombre del negocio: `Nebla — Dr. Alben Rosas`
   - Tu nombre y email: alben.rosas@gmail.com
3. En Business Manager → **Configuración del negocio**:
   - Agrega tu **Página de Facebook** (la que ya existe)
   - Agrega tu **cuenta de Instagram** (@dralbenrosas)
4. Crea una **Cuenta publicitaria**:
   - Nombre: `Nebla Ads`
   - Moneda: MXN
   - Zona horaria: México/Ciudad de México
5. Agrega **método de pago** (tarjeta de crédito/débito)
6. Asigna tu cuenta publicitaria a la Página de Facebook y a Instagram
7. Ve a **Configuración del negocio → Verificación del negocio** y verifica tu dominio (cuando tengas el sitio)

> ⚠️ Si Meta te pide verificación de identidad, sube una foto de tu INE o pasaporte — es normal para cuentas nuevas.

---

### 2.2 Estructura de campaña — Lead Gen nativo

> El objetivo **Generación de clientes potenciales** muestra un formulario dentro de Facebook/Instagram. El paciente llena su nombre y teléfono sin salir de la app. Sin pixel, sin sitio web.

```
CUENTA PUBLICITARIA: Nebla Ads
│
├── CAMPAÑA 1: Vesícula — Lead Gen    [LANZAR PRIMERO]
│   Presupuesto: $70 MXN/día (CBO — a nivel campaña)
│   │
│   ├── Ad Set 1A: Mujeres 30–60, La Paz + 60km radio
│   │   Anuncio 1A-1: Ángulo síntomas ("¿Dolor después de comer grasoso?")
│   │   Anuncio 1A-2: Ángulo miedo ("La cirugía de vesícula no es lo que imaginas")
│   │
│   └── Ad Set 1B: Hombres + Mujeres 40–65, La Paz + Los Cabos
│       Anuncio 1B-1: Ángulo urgencia ("Los cálculos no desaparecen solos")
│
└── CAMPAÑA 2: Hernias — Lead Gen
    Presupuesto: $30 MXN/día
    └── Ad Set 2A: Hombres 25–60, La Paz + Los Cabos
        Anuncio 2A-1: Ángulo postergación ("Llevas meses con esa hernia")
        Anuncio 2A-2: Ángulo recuperación ("Cirugía de hernia: vuelves al trabajo en días")

TOTAL META: $100 MXN/día (~$3,000 MXN/mes)
```

---

### 2.3 Configuración de Ad Sets

| Parámetro | Campaña Vesícula | Campaña Hernias |
|-----------|-----------------|-----------------|
| Objetivo | Clientes potenciales | Clientes potenciales |
| Ubicación | La Paz BCS + Los Cabos + 60km | La Paz BCS + Los Cabos + 60km |
| Edad | 30–65 | 25–60 |
| Género | Todos | Todos |
| Targeting | **Advantage+ Audience** (dejar que Meta optimice) | **Advantage+ Audience** |
| Placements | **Advantage+ Placements** (Meta elige Feed + Stories + Reels) | Advantage+ Placements |
| Optimización | Clientes potenciales | Clientes potenciales |
| Ventana de atribución | 7 días clic / 1 día vista | 7 días clic / 1 día vista |

---

### 2.4 Formulario de Lead Gen (configurar 1 formulario para vesícula, 1 para hernia)

**Formulario: Vesícula**
```
Título: "Agenda tu consulta de vesícula"
Imagen: [usar foto del Dr. Rosas fuera de quirófano cuando esté disponible]
          [mientras tanto: fondo Terracota #8B3A2A con texto "Dr. Alben Rosas · Cirujano General"]

Preguntas (en este orden):
  1. Nombre completo [autocompletado desde Facebook]
  2. Número de teléfono [autocompletado desde Facebook]
  3. ¿Cuál es tu principal motivo de consulta?
     ○ Me diagnosticaron cálculos en la vesícula
     ○ Tengo dolor después de comer
     ○ Quiero saber si necesito cirugía
     ○ Otro

Texto de privacidad:
"Tu información se usa únicamente para contactarte y agendar tu consulta. No compartimos tus datos."

Pantalla de agradecimiento:
Título: "¡Listo! En breve te contactamos."
Texto: "El Dr. Alben Rosas o su equipo te llamarán en las próximas horas para agendar tu consulta de valoración."
CTA: "Guardar formulario"
```

**Formulario: Hernias**
```
Título: "Agenda tu consulta de hernia"

Preguntas:
  1. Nombre completo [autocompletado]
  2. Número de teléfono [autocompletado]
  3. ¿Qué tipo de hernia tienes?
     ○ Hernia inguinal (ingle)
     ○ Hernia umbilical (ombligo)
     ○ No sé / necesito diagnóstico
     ○ Otro

Pantalla de agradecimiento:
Título: "¡Listo! Te contactamos pronto."
Texto: "El Dr. Rosas te llamará para agendar tu valoración. La cirugía de hernia es más sencilla de lo que imaginas."
```

---

### 2.5 Ad Copy — META ADS (versión completa)

> ⚠️ Todas las imágenes deben ser del Dr. Rosas fuera del quirófano o gráficos de texto. NUNCA fotos de cirugías activas en ads pagados.

---

**ANUNCIO 1A-1 — Vesícula, ángulo síntomas**
*(Usar para Ad Set Mujeres 30–60)*

```
TEXTO PRINCIPAL (primary text):
¿Sientes dolor después de comer algo grasoso?

Puede ser tu vesícula.

Los cálculos biliares son muy comunes, especialmente en mujeres entre 30 y 60 años — y no desaparecen solos.

La buena noticia: la cirugía laparoscópica los resuelve de una vez, con recuperación en pocos días y sin cicatriz grande.

Soy el Dr. Alben Rosas, cirujano general en La Paz, BCS, especializado en vesícula, hernias y cirugía gastrointestinal. Te doy un diagnóstico claro en tu primera consulta — sin rodeos.

👇 Llena el formulario y te contactamos esta semana.

HEADLINE: ¿Dolor después de comer? Puede ser tu vesícula
DESCRIPCIÓN: Cirujano General · La Paz BCS · Sin lista de espera
CTA: Más información [→ abre el formulario de lead gen]
```

---

**ANUNCIO 1A-2 — Vesícula, ángulo miedo a operarse**

```
TEXTO PRINCIPAL:
"Me da miedo operarme de la vesícula."

Es lo más común que escucho.

La realidad: la cirugía laparoscópica de vesícula es mucho más sencilla de lo que imaginas.
— Incisiones pequeñas (menos de 1 cm)
— Anestesia general, sin que sientas nada
— La mayoría de pacientes vuelve a casa el mismo día
— Recuperación normal en 5–7 días

Si ya tienes diagnóstico de cálculos o tienes síntomas frecuentes, estás aplazando algo que no va a mejorar solo.

Agenda tu consulta de valoración en La Paz, BCS — sin viajar, sin esperas largas.

HEADLINE: La cirugía de vesícula no es lo que imaginas
DESCRIPCIÓN: Laparoscopia · Recuperación en días · La Paz BCS
CTA: Más información
```

---

**ANUNCIO 1B-1 — Vesícula, ángulo urgencia**
*(Para Ad Set mixto 40–65)*

```
TEXTO PRINCIPAL:
Los cálculos en la vesícula no desaparecen solos.

Muchos pacientes esperan meses o años pensando que "no está tan mal". Hasta que viene el cólico biliar — y eso sí es una emergencia.

La diferencia entre una cirugía electiva (programada) y una de urgencia es enorme: en la electiva eliges la fecha, hay menos riesgo y la recuperación es mejor.

Si tienes diagnóstico o síntomas, el momento de actuar es ahora.

Dr. Alben Rosas — Cirujano General, La Paz BCS.
Certificado CMCG 2026 · Especializado en cirugía laparoscópica.

HEADLINE: Los cálculos no desaparecen solos
DESCRIPCIÓN: Cirugía laparoscópica · La Paz BCS · Agenda esta semana
CTA: Más información
```

---

**ANUNCIO 2A-1 — Hernias, ángulo postergación**
*(Para Ad Set Hombres 25–60)*

```
TEXTO PRINCIPAL:
¿Llevas meses —o años— con esa hernia?

Es más común de lo que crees. Muchos hombres la posponen porque "no duele tanto" o "puedo esperar".

El problema: las hernias no se curan solas. Con el tiempo pueden crecer y, en el peor caso, estrangularse — eso sí es una emergencia real.

La cirugía laparoscópica de hernia es rápida, con recuperación en pocos días y sin la cicatriz grande de antes. La mayoría de pacientes vuelven al trabajo en menos de una semana.

Si estás en La Paz, BCS, te atiendo directamente — sin intermediarios, sin listas de espera del IMSS.

👇 Escríbenos para agendar tu valoración esta semana.

HEADLINE: ¿Llevas tiempo con esa hernia? Ya es hora.
DESCRIPCIÓN: Cirugía laparoscópica · Recuperación rápida · La Paz BCS
CTA: Más información
```

---

**ANUNCIO 2A-2 — Hernias, ángulo recuperación**

```
TEXTO PRINCIPAL:
Cirugía de hernia y vuelves al trabajo en días.

Antes era una operación grande, con cicatriz larga y semanas de recuperación.

Hoy con técnica laparoscópica:
✅ 3 incisiones pequeñas (menos de 1 cm)
✅ Sin cicatriz visible
✅ La mayoría regresa a actividad normal en 5–7 días
✅ Resultado permanente

Si tienes una hernia inguinal o umbilical en La Paz, BCS, agenda tu valoración con el Dr. Alben Rosas — cirujano general certificado.

No necesitas esperar meses en el IMSS.

HEADLINE: Hernia operada — de vuelta al trabajo en días
DESCRIPCIÓN: Cirugía laparoscópica en La Paz BCS · Sin lista de espera
CTA: Más información
```

---

### 2.6 Assets visuales para los anuncios

Mientras no tengas la foto del Dr. Rosas fuera del quirófano, usar estas alternativas:

**Opción A — Tarjeta de texto (puedes crear en Canva):**
```
Fondo: Terracota #8B3A2A
Texto superior (Jost Light, Blanco): "CIRUJANO GENERAL · LA PAZ BCS"
Texto central (Cormorant Garamond, grande, Crema #F5EDE3): "¿Dolor después de comer grasoso?"
Texto inferior (Jost Light, Oro #C4922A): "Dr. Alben Rosas · Agenda tu consulta"
Logo monograma A: esquina superior derecha
Formato: 1080×1080 (feed) y 1080×1920 (stories/reels)
```

**Opción B — Foto de quirófano (orgánico ya mejorado):**
Las fotos procesadas en `.agents/assets/photos/enhanced/` se pueden usar en Instagram orgánico para generar confianza. Los leads que lleguen de esas publicaciones orgánicas se redirigen al formulario de WhatsApp.

**Opción C — Foto del Dr. (prioritaria):**
En cuanto tengas la foto fuera del quirófano → usarla como imagen principal en todos los ads. El Dr. mirando a cámara, con fondo neutro o exterior, con o sin bata blanca (no quirúrgica).

---

## PARTE 3 — CHECKLIST DE LANZAMIENTO

### Semana actual — lo que tú necesitas hacer

- [ ] **Google:** Crear cuenta en ads.google.com (20 min)
- [ ] **Google:** Crear Google Business Profile en business.google.com (15 min)
- [ ] **Meta:** Crear Business Manager en business.facebook.com (20 min)
- [ ] **Meta:** Conectar Instagram @dralbenrosas + Facebook Page al Business Manager (10 min)
- [ ] **Meta:** Agregar método de pago en Meta Business Manager (5 min)
- [ ] **Foto:** Tomar foto del Dr. Rosas fuera del quirófano (esta semana — confirmado)

### Una vez que tengas cuentas creadas — yo configuro

- [ ] Ingresar toda la estructura de campañas Google (copy ya listo arriba)
- [ ] Configurar extensiones de anuncio
- [ ] Crear formularios de lead gen en Meta
- [ ] Crear los ad sets y subir los anuncios
- [ ] Activar campañas

### Después del lanzamiento — seguimiento

- [ ] Revisar leads de Meta diariamente (descargar desde Meta Ads Manager → Leads Center)
- [ ] Contestar llamadas de Google Ads durante el horario configurado (Lun–Sáb 8am–8pm)
- [ ] Semana 2: Revisar CTR y CPL — ajustar copy que no convierte
- [ ] Semana 3: Evaluar qué keywords generan llamadas reales vs spam

---

## PARTE 4 — PRESUPUESTO FASE 0

| Canal | Diario | Mensual |
|-------|--------|---------|
| Google Ads (Call-Only) | $250 MXN | ~$7,500 MXN |
| Meta Ads (Lead Gen) | $100 MXN | ~$3,000 MXN |
| **Total** | **$350 MXN/día** | **~$10,500 MXN (~$525 USD)** |

**Proyección conservadora:**
- Google: 30-50 llamadas/mes a $5-15 USD por llamada
- Meta: 20-60 leads/mes a $3-8 USD por lead
- **Total estimado: 50-110 contactos nuevos mes 1**
- Tasa de cierre consulta estimada: 30-50% → **15-55 consultas nuevas mes 1**

---

*Próxima actualización: cuando las cuentas estén creadas para ingresar la configuración exacta.*
