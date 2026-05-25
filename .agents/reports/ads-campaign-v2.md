# Ads Campaign — Versión 2 (Sitio web live)
*Actualizado: 2026-05-25 | Basado en análisis de dralbenrosas.com*

> Cambio vs Fase 0: ahora usamos Search normal (con URL del sitio) en lugar de Call-Only. Meta Ads también apuntan al sitio. El sitio es una sola página — todos los anuncios apuntan a `https://dralbenrosas.com/` con UTMs.

---

## ANÁLISIS DEL SITIO

### Lo que tiene el sitio ✅
| Elemento | Detalle |
|----------|---------|
| Hero | "Cirugía clara, cirugía oportuna" — excelente hook |
| CTA principal | "Agendar por WhatsApp" (botón verde) + "Llamar al consultorio" |
| CTA flotante | Burbuja WhatsApp en esquina inferior derecha |
| Estadísticas | 7-14 días a cirugía · 9 meses sin intereses · 15 días postop · 100% paquete cerrado |
| Servicios | Vesícula · Hernias · Cirugía urgencia · Cirugía digestiva |
| Diferenciadores | Claridad clínica · Cirugía oportuna · Pago accesible · Postop cercano |
| Diseño | Cormorant Garamond + paleta Crema/Terracota — on brand |

### Lo que falta ⚠️
| Elemento | Prioridad | Acción |
|----------|-----------|--------|
| Tracking (GTM, GA4, Pixel) | 🔴 Crítico | Ver tracking-setup.md |
| Foto del Dr. Rosas | 🔴 Alta | Pendiente sesión fotográfica |
| Páginas individuales por servicio | 🟢 Baja | Útil para Mes 2+ pero no bloquea lanzamiento |

### Activos descubiertos en el sitio ✅ (usar en ads)
| Activo | Dónde usar |
|--------|-----------|
| Quiz cotizador "3 toques" | Headline Google: "Cotiza tu cirugía en 30 segundos" |
| Testimonio Jorge R. (hernia) | Copy Meta: citar textual |
| Testimonio Lourdes M. (hernia) | Copy Meta: citar textual |
| "Respuesta en menos de 2 horas" | Callout extension Google + copy Meta |
| "Sin filtros ni call centers" | Diferenciador en copy |
| Dirección: Médica del Cortés, Blvd. Pino Pallas 104 | Google Business Profile + extensión ubicación |

### Datos de contacto CORRECTOS (actualizar todo lo anterior)
| Canal | Número |
|-------|--------|
| **WhatsApp (conversión principal)** | **+52 663 437 0584** → wa.me/526634370584 |
| Teléfono consultorio | +52 612 146 7076 (Lun-Vie) |
| Consultorio | Médica del Cortés, Blvd. Pino Pallas 104, La Paz BCS |

### Nuevos diferenciadores a incorporar en el copy de ads
Estos aparecen en el sitio pero no estaban en la v1 de nuestros anuncios:
1. **"7-14 días a cirugía"** — responde directamente la objeción IMSS
2. **"Paquete todo incluido, 9 meses sin intereses"** — elimina miedo al costo
3. **"Cotización por escrito antes de operar"** — transparencia total
4. **"WhatsApp directo con el Dr. 15 días después de tu cirugía"** — postop cercano

---

## ESTRUCTURA DE CAMPAÑAS

### Google Ads — Search (con landing page real)

```
URL base de destino: https://dralbenrosas.com/
UTM structure: ?utm_source=google&utm_medium=cpc&utm_campaign={campaign_name}&utm_content={adgroup}&utm_term={keyword}

CUENTA: Nebla — Dr. Alben Rosas
│
├── CAMPAÑA 1: Vesícula [PRIORIDAD 1]
│   Presupuesto: $130 MXN/día
│   Estrategia: CPC manual, max $35 MXN/clic
│   ├── Grupo 1A: Síntomas vesícula
│   ├── Grupo 1B: Cirugía vesícula (alta intención)
│   └── Grupo 1C: Urgencia biliar
│
├── CAMPAÑA 2: Hernias [PRIORIDAD 2]
│   Presupuesto: $70 MXN/día
│   ├── Grupo 2A: Síntomas hernia
│   └── Grupo 2B: Cirugía hernia
│
├── CAMPAÑA 3: Cirujano General / Branded [PRIORIDAD 3]
│   Presupuesto: $30 MXN/día
│   └── Grupo 3A: Cirujano La Paz BCS + branded
│
└── CAMPAÑA 4: Urgencias + GI [PRIORIDAD 4, agregar en Mes 2]
    Presupuesto: $20 MXN/día

TOTAL GOOGLE: $230 MXN/día (~$6,900 MXN/mes)
```

---

## AD COPY — GOOGLE ADS v2
*(RSA — Responsive Search Ads. Google combina los headlines y descriptions automáticamente.)*

### CAMPAÑA 1 — VESÍCULA, Grupo 1A: Síntomas

**Keywords (concordancia de frase y exacta):**
```
[cálculos en la vesícula]
[dolor de vesícula]
"piedras en la vesícula"
"vesícula inflamada"
"síntomas de vesícula"
"cólico biliar"
"dolor después de comer grasoso"
"qué hacer con cálculos en la vesícula"
```

**RSA Headlines (15 máx, Google elige 3 por vez — max 30 chars c/u):**
```
1.  ¿Dolor en la vesícula? [24]
2.  Cálculos en vesícula, La Paz [30]
3.  Cirugía en 7 a 14 días [25]
4.  Sin esperar meses en el IMSS [30]
5.  Especialista en vesícula BCS [30]
6.  Diagnóstico claro en consulta [30]
7.  Paquete todo incluido [22]
8.  9 meses sin intereses [22]
9.  Alta el mismo día de la cirugía [32 ⚠️ recortar]
10. Alta el mismo día [18]
11. Sin cicatriz grande — laparoscopia [35 ⚠️ recortar]
12. Laparoscopía, sin cicatriz [28]
13. Cirujano Dr. Alben Rosas [26]
14. La Paz BCS — agenda hoy [25]
15. Cotización por escrito [23]
```

**Headlines corregidos a 30 chars:**
```
1.  ¿Dolor en la vesícula?         [24 ✓]
2.  Cálculos vesícula — La Paz     [29 ✓]
3.  Cirugía en 7 a 14 días         [25 ✓]
4.  Sin esperar meses en el IMSS   [30 ✓]
5.  Especialista vesícula La Paz   [30 ✓]
6.  Diagnóstico claro en consulta  [30 ✓]
7.  Paquete todo incluido          [22 ✓]
8.  9 meses sin intereses          [22 ✓]
9.  Alta el mismo día              [18 ✓]
10. Laparoscopía, sin cicatriz     [28 ✓]
11. Cirujano Dr. Alben Rosas       [26 ✓]
12. La Paz BCS — agenda hoy        [25 ✓]
13. Cotización por escrito         [23 ✓]
14. Atención directa con el Dr.    [28 ✓]
15. Sin sorpresas de costo         [22 ✓]
```

**RSA Descriptions (4 máx, max 90 chars c/u):**
```
1. Cirugía de vesícula en La Paz, BCS. Programación en 7-14 días, paquete todo incluido.    [83 ✓]
2. ¿Te dijeron que tienes cálculos? Diagnóstico claro, sin tecnicismos. Agenda esta semana. [88 ✓]
3. Laparoscopía: alta el mismo día, recuperación rápida. Sin las esperas del sistema público.[90 ✓]
4. Paquetes cerrados, 9 meses sin intereses. Cotización por escrito antes de operar.         [82 ✓]
```

---

### CAMPAÑA 1 — VESÍCULA, Grupo 1B: Cirugía (alta intención)

**Keywords:**
```
[cirugía de vesícula La Paz]
[operación de vesícula La Paz]
[colecistectomía La Paz BCS]
[cirugía laparoscópica vesícula La Paz]
"cirujano de vesícula La Paz"
"colecistectomía laparoscópica La Paz"
```

**Headlines:**
```
1.  Cirugía Vesícula La Paz BCS    [27 ✓]
2.  Colecistectomía Laparoscópica  [30 ✓]
3.  Cirugía en 7 a 14 Días         [24 ✓]
4.  Sin Viajar a Guadalajara       [27 ✓]
5.  Paquete Todo Incluido          [22 ✓]
6.  Alta el Mismo Día              [18 ✓]
7.  Especialista en Vesícula       [24 ✓]
8.  9 Meses Sin Intereses          [22 ✓]
9.  Dr. Alben Rosas, La Paz BCS    [27 ✓]
10. Cotización por Escrito         [23 ✓]
```

**Descriptions:**
```
1. Cirugía laparoscópica de vesícula en La Paz. Paquete cerrado, 9 meses sin intereses.     [83 ✓]
2. Programa tu cirugía en 7 a 14 días. Sin cicatriz grande, alta el mismo día en la mayoría.[89 ✓]
3. Cirujano certificado CMCG. Trato directo desde la consulta hasta el postoperatorio.       [82 ✓]
4. Sin viajar a Guadalajara. Hospitales privados en La Paz, BCS. Cotización por escrito.    [83 ✓]
```

---

### CAMPAÑA 2 — HERNIAS

**Keywords:**
```
[hernia inguinal La Paz]
[hernia umbilical La Paz]
[cirugía de hernia La Paz]
"operación de hernia La Paz BCS"
"hernia inguinal cirujano La Paz"
"hernia laparoscópica La Paz"
"bulto en la ingle La Paz"
```

**Headlines:**
```
1.  Cirugía Hernia La Paz BCS      [27 ✓]
2.  Hernia Inguinal o Umbilical    [28 ✓]
3.  Cirugía en 7 a 14 Días         [24 ✓]
4.  Vuelta al Trabajo en Días      [27 ✓]
5.  Paquete Todo Incluido          [22 ✓]
6.  Malla Última Generación        [24 ✓]
7.  Sin Esperar en el IMSS         [22 ✓]
8.  Cirujano Dr. Alben Rosas       [26 ✓]
9.  9 Meses Sin Intereses          [22 ✓]
10. La Paz BCS — Agenda Hoy        [25 ✓]
```

**Descriptions:**
```
1. Hernia inguinal, umbilical o abdominal en La Paz, BCS. Cirugía laparoscópica, malla última gen.[96 ⚠️]
1. Hernia inguinal o umbilical en La Paz, BCS. Reparación laparoscópica, malla de última gen.  [88 ✓]
2. Programación quirúrgica en 7-14 días. Paquete cerrado, cotización por escrito, sin sorpresas. [90 ✓]
3. La hernia no mejora sola. Cirugía rápida, recuperación en días. Sin espera del sistema público.[90 ✓]
4. Dr. Alben Rosas, cirujano certificado CMCG. WhatsApp directo 15 días postoperatorio.          [85 ✓]
```

---

### CAMPAÑA 3 — CIRUJANO GENERAL / BRANDED

**Keywords:**
```
[cirujano general La Paz BCS]
[cirujano La Paz BCS]
[cirugía laparoscópica La Paz]
"dr alben rosas"
"dralbenrosas"
"nebla cirujano"
"cirujano privado La Paz"
```

**Headlines:**
```
1.  Cirujano General La Paz BCS    [28 ✓]
2.  Dr. Alben Rosas — Cirujano     [27 ✓]
3.  Vesícula, Hernias y Más        [25 ✓]
4.  Cirugía en 7 a 14 Días         [24 ✓]
5.  Paquete Todo Incluido          [22 ✓]
6.  Certificado CMCG 2026          [21 ✓]
7.  Postop 15 Días por WhatsApp    [28 ✓]
8.  Sin Sorpresas de Costo         [22 ✓]
```

**Descriptions:**
```
1. Cirujano general certificado en La Paz, BCS. Vesícula, hernias, urgencias y cirugía GI.   [85 ✓]
2. Cirugía en 7-14 días, paquete cerrado, 9 meses sin intereses. Agenda tu consulta hoy.     [82 ✓]
```

---

### Extensiones de anuncio (configurar en TODAS las campañas)

**Extensión de llamada:**
```
Número consultorio: +52 612 146 7076
Horario: Lunes–Viernes, 9:00 AM – 6:00 PM
```

**Extensión de sitelinks:**
```
Texto: Vesícula biliar           URL: https://dralbenrosas.com/?utm_content=sitelink_vesicula
Texto: Cirugía de hernia         URL: https://dralbenrosas.com/?utm_content=sitelink_hernia
Texto: Cirugía de urgencia       URL: https://dralbenrosas.com/?utm_content=sitelink_urgencia
Texto: Agendar por WhatsApp      URL: https://dralbenrosas.com/?utm_content=sitelink_whatsapp
```

**Extensión de texto destacado (callouts):**
```
7-14 días a cirugía | Paquete todo incluido | 9 meses sin intereses | Respuesta en menos de 2 horas | Postop 15 días WhatsApp | Certificado CMCG | Sin call centers
```

**Extensión de fragmento de sitio:**
```
Cabecera: Especialidades
Valores: Vesícula biliar · Hernias · Cirugía de urgencia · Cirugía digestiva
```

---

### Negative Keywords (todas las campañas)

```
IMSS, ISSSTE, seguro popular, gratuito, gratis, costo cero, sin costo,
veterinario, cirujano plástico, estética, liposucción, bariátrica, bypass gástrico,
Guadalajara, CDMX, Tijuana, Mexicali, Monterrey, Hermosillo,
empleo, trabajo, sueldo, vacante, plaza,
pediatra, oncólogo, ginecólogo, dentista,
YouTube, video, tutorial, cómo, qué es,
receta, medicamento, pastilla, natural, remedio
```

---

## CONFIGURACIÓN GOOGLE ADS

| Parámetro | Valor |
|-----------|-------|
| Tipo de campaña | Búsqueda |
| Objetivo | Clientes potenciales |
| Red | Solo búsqueda (desactivar Display y socios al inicio) |
| Ubicación | La Paz, BCS → radio 60 km |
| Idioma | Español |
| Estrategia de puja | CPC manual → cambiar a "Maximizar conversiones" cuando tengas 30+ conversiones/mes |
| URL final | `https://dralbenrosas.com/` + UTMs |
| Conversión | WhatsApp click (configurado en GTM — ver tracking-setup.md) |
| Rotación | Optimizar: mejor rendimiento |
| Programación | Lun–Sáb 7am–9pm (cuando puedes contestar WhatsApp) |

---

## META ADS — v2 (con destino al sitio web)

### Cambio vs Fase 0
- **Antes:** Lead Gen nativo (sin sitio)
- **Ahora:** Tráfico → dralbenrosas.com → clic en WhatsApp = conversión
- **Ventaja:** El Pixel registra PageViews para crear audiencias de remarketing

### Configuración de campaña

| Parámetro | Valor |
|-----------|-------|
| Objetivo | Leads (o Tráfico hasta tener el Pixel instalado) |
| Optimización | WhatsApp click (event Lead en Pixel) |
| URL destino | `https://dralbenrosas.com/?utm_source=meta&utm_medium=paid_social&utm_campaign=X` |
| Ubicación | La Paz BCS + Los Cabos + radio 60km |
| Edad | 28–65 |
| Targeting | Advantage+ Audience (dejar que Meta optimice) |
| Placements | Advantage+ Placements |
| Presupuesto | CBO a nivel campaña |

### Estructura Meta

```
CAMPAÑA 1: Vesícula — $70 MXN/día (CBO)
  Ad Set 1A: Mujeres 30-60
    Anuncio A: "¿Dolor después de comer grasoso?" (copy síntomas)
    Anuncio B: "La cirugía de vesícula no es lo que imaginas" (copy miedo)
    Anuncio C: "Cirugía en 7 días, paquete todo incluido" (copy logístico — NUEVO)

  Ad Set 1B: Todos 40-65
    Anuncio D: "9 meses sin intereses para tu cirugía" (copy financiero — NUEVO)

CAMPAÑA 2: Hernias — $30 MXN/día (CBO)
  Ad Set 2A: Hombres 25-60
    Anuncio A: "Llevas meses con esa hernia" (copy postergación)
    Anuncio B: "Hernia operada, de vuelta al trabajo en días" (copy recuperación)

TOTAL META: $100 MXN/día (~$3,000 MXN/mes)
```

---

## AD COPY META — v2 (incorpora diferenciadores del sitio)

### ANUNCIO NUEVO — Ángulo logístico/rapidez

```
TEXTO PRINCIPAL:
¿Cuándo me puedo operar?

Eso es lo primero que me preguntan.

La respuesta: en 7 a 14 días desde tu primera consulta.

Sin listas de espera de meses. Sin incertidumbre de fechas.
El día de tu cirugía lo defines tú — dentro de ese rango.

Vesícula, hernia o cualquier procedimiento electivo de cirugía general
en La Paz, BCS, con el Dr. Alben Rosas.

Paquete cerrado, todo incluido. Cotización por escrito antes de que decidas.

👇 Escríbeme por WhatsApp para agendar tu consulta esta semana.

HEADLINE: Cirugía en 7 a 14 días — sin esperas
DESCRIPCIÓN: Paquete todo incluido · La Paz BCS · Sin sorpresas
CTA: Más información
```

---

### ANUNCIO NUEVO — Ángulo financiero / paquete cerrado

```
TEXTO PRINCIPAL:
"¿Y cuánto sale todo?"

Esa pregunta me la hacen en cada consulta.

Por eso trabajo con paquetes cerrados:
✅ Cirugía
✅ Anestesia
✅ Sala de operaciones
✅ Material quirúrgico
✅ Postoperatorio 15 días
Todo en un solo precio. Sin sorpresas al final.

Y si necesitas financiarlo: hasta 9 meses sin intereses.
Te doy la cotización por escrito antes de que decidas operarte.

Soy el Dr. Alben Rosas, cirujano general en La Paz, BCS.

HEADLINE: Paquete todo incluido — sin sorpresas de costo
DESCRIPCIÓN: 9 meses sin intereses · Cotización por escrito · La Paz BCS
CTA: Más información
```

---

### ANUNCIO — Vesícula síntomas (actualizado con diferenciadores)

```
TEXTO PRINCIPAL:
¿Sientes dolor después de comer algo grasoso?

Puede ser tu vesícula.

Los cálculos biliares no desaparecen solos — pero resolverlos es más
sencillo de lo que imaginas:

→ Consulta de valoración
→ Cirugía laparoscópica programada en 7 a 14 días
→ Alta el mismo día en la mayoría de casos
→ Recuperación normal en menos de una semana

Trabajo con paquete todo incluido. Sin costos ocultos.
9 meses sin intereses disponibles.

Soy el Dr. Alben Rosas, cirujano general certificado en La Paz, BCS.

HEADLINE: ¿Dolor después de comer? Puede ser tu vesícula
DESCRIPCIÓN: Cirugía en 7-14 días · Paquete todo incluido · La Paz BCS
CTA: Más información
```

---

### ANUNCIO — Miedo a operar (actualizado)

```
TEXTO PRINCIPAL:
"Me da miedo operarme de la vesícula."

Es lo más común que escucho en consulta.

Por eso trabajo diferente:

Antes de que decidas operar te doy todo por escrito:
— Diagnóstico explicado con tus propios estudios
— Plan quirúrgico detallado
— Cotización cerrada: lo que cuesta es lo que pagas
— Fecha de cirugía que tú eliges (7 a 14 días)

Y después de la cirugía: mi WhatsApp directo durante 15 días.
Sin filtros, sin secretaria, sin esperar.

HEADLINE: La cirugía de vesícula no es lo que imaginas
DESCRIPCIÓN: Todo por escrito antes de operar · La Paz BCS
CTA: Más información
```

---

---

### ANUNCIO — Testimonio (social proof, hernia)

```
TEXTO PRINCIPAL:
"Buscaba un cirujano que no me apurara. Me dio segunda opinión clara,
me operó cuando fue necesario. Cumplió todo lo que prometió."
— Jorge R., hernia inguinal · 2026 ⭐⭐⭐⭐⭐

Eso es lo que me propongo con cada paciente.

Sin presionar. Sin vender la cirugía si no es necesaria.
Te explico tu caso, te doy opciones, y decides tú.

Si tienes una hernia y quieres una valoración honesta:

Dr. Alben Rosas — Cirujano General, La Paz BCS
Programación en 7-14 días · Paquete cerrado · MSI disponibles

HEADLINE: "Cumplió todo lo que prometió" — Jorge R.
DESCRIPCIÓN: Cirugía de hernia en La Paz BCS · Sin presiones · Cotización por escrito
CTA: Más información
```

---

### ANUNCIO — Testimonio (social proof, costo)

```
TEXTO PRINCIPAL:
"Atención a un nivel que no esperaba. Cotización por escrito sin sorpresas,
MSI funcionaron, y lo más importante: trato humano de inicio a fin."
— Lourdes M., hernia umbilical · 2026 ⭐⭐⭐⭐⭐

El miedo al costo es normal. Por eso trabajo diferente:

Antes de que decidas te doy todo por escrito:
el precio exacto, qué incluye, y las opciones de pago.
Sin sorpresas al final.

Hasta 9 meses sin intereses disponibles.

Dr. Alben Rosas — Cirujano General, La Paz BCS

HEADLINE: "Cotización sin sorpresas" — paciente real ⭐⭐⭐⭐⭐
DESCRIPCIÓN: Paquete cerrado · 9 MSI · Trato directo · La Paz BCS
CTA: Más información
```

---

### ANUNCIO — Quiz/Cotizador (nuevo ángulo de entrada)

```
TEXTO PRINCIPAL:
¿Cuánto cuesta tu cirugía?

Te lo digo en 30 segundos.

En el sitio tenemos un cotizador de 3 preguntas:
1. ¿Qué te trae? (vesícula, hernia, otro)
2. ¿Cuándo te interesa operar?
3. ¿Cómo prefieres pagar?

Sin formularios largos. Sin esperar días.
Sin que te llame alguien que no es el médico.

Entra, cotiza, y si te convence: escribes directo al Dr.

HEADLINE: Cotiza tu cirugía en 30 segundos
DESCRIPCIÓN: 3 preguntas · Paquete cerrado · La Paz BCS · Sin compromiso
CTA: Más información  [→ apunta a dralbenrosas.com/#cotizador]
```

---

## PRESUPUESTO TOTAL — MES 1

| Canal | Diario | Mensual | Métrica objetivo |
|-------|--------|---------|-----------------|
| Google Search | $230 MXN | ~$6,900 MXN | 20-60 clics WhatsApp/mes |
| Meta Ads | $100 MXN | ~$3,000 MXN | 15-45 clics al sitio que convierten |
| **Total** | **$330 MXN/día** | **~$9,900 MXN (~$500 USD)** | **35-105 contactos nuevos mes 1** |

---

## CHECKLIST PARA LANZAR

### Bloquea el lanzamiento (sin esto no arrancamos):
- [ ] Tracking instalado: GTM en `<head>` + `<body>` del sitio
- [ ] GA4 configurado en GTM
- [ ] Meta Pixel configurado en GTM
- [ ] Evento "WhatsApp click" disparando correctamente (verificar con Tag Assistant)
- [ ] Meta Business Manager creado
- [ ] Cuenta Google Ads creada

### Importante pero no bloquea:
- [ ] Google Business Profile creado y verificado
- [ ] Foto del Dr. Rosas fuera de quirófano (para imagen de Meta Ads)
- [ ] Conversión Google Ads configurada en GTM

### Para Mes 2:
- [ ] Cambiar estrategia de puja a "Maximizar conversiones" (cuando tenga 30+ conv/mes)
- [ ] Crear audiencia de remarketing (visitantes del sitio últimos 30 días)
- [ ] Campaña de remarketing Meta (pacientes que visitaron pero no escribieron por WhatsApp)
- [ ] Evaluar crear páginas separadas por servicio para mejorar Quality Score
