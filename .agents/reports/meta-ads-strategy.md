# Estrategia Meta Ads — Dr. Alben Rosas / Cirugía General
*La Paz + Los Cabos BCS | Pixel: 3456701621158975 | Actualizado: 2026-05-25*

---

## 1. ESTRUCTURA DE CAMPAÑAS

Tres campañas siempre activas, cada una con un objetivo distinto.

```
CUENTA META ADS
│
├── 🎯 Campaña 1: Conversiones — Captación Activa      (60% del presupuesto)
│   ├── Ad Set 1A: Vesícula — Mujeres 30-60
│   ├── Ad Set 1B: Hernias — Hombres 35-65
│   └── Ad Set 1C: Dolor abdominal — Mixto 30-60
│
├── 🔁 Campaña 2: Remarketing — Visitantes sin agendar  (25% del presupuesto)
│   └── Ad Set 2A: Visitantes web últimos 60 días
│
└── 📣 Campaña 3: Reconocimiento Local                 (15% del presupuesto)
    └── Ad Set 3A: La Paz + Los Cabos, amplio
```

### Campaña 1 — Conversiones (captación activa)

| Campo | Configuración |
|-------|--------------|
| Objetivo | Clientes potenciales → Conversión en sitio web |
| Evento de conversión | `Lead` (Pixel 3456701621158975) |
| Estrategia de puja | Costo por resultado más bajo (automático al inicio) |
| Ubicaciones | Manual: Feed Facebook + Feed Instagram + Reels (excluir Audience Network) |
| Presupuesto | Ver Sección 4 |

**Ad Set 1A — Vesícula (mujeres)**
- Género: Mujeres
- Edad: 30-60 años
- Geografía: La Paz BCS + Los Cabos (radio 80 km cada uno)
- Intereses: salud, bienestar, familia, seguros médicos, nutrición
- Exclusión: audiencia "Ya agendaron" (Lead event)

**Ad Set 1B — Hernias (hombres)**
- Género: Hombres
- Edad: 35-65 años
- Geografía: misma
- Intereses: construcción, trabajo manual, deporte, seguros, salud masculina
- Exclusión: audiencia "Ya agendaron"

**Ad Set 1C — Dolor abdominal / Valoración (amplio)**
- Género: Todos
- Edad: 30-65 años
- Geografía: misma
- Intereses: salud, medicina privada, IMSS (para excluir quienes prefieren IMSS)
- Sin restricción de género — captura síntomas que no pertenecen a 1A o 1B

---

### Campaña 2 — Remarketing

| Campo | Configuración |
|-------|--------------|
| Objetivo | Clientes potenciales → Conversión en sitio web |
| Audiencia | Custom Audience: Visitantes web últimos 60 días |
| Exclusión | Custom Audience: Personas que ya hicieron clic en WhatsApp (Lead event) |
| Frecuencia | Cap: máximo 3 impresiones por semana por persona |
| Copy | Más urgente: "Todavía hay lugar esta semana" |

---

### Campaña 3 — Reconocimiento local

| Campo | Configuración |
|-------|--------------|
| Objetivo | Alcance |
| Audiencia | La Paz + Los Cabos, 30-65, amplio sin intereses |
| Formato | Video corto (30 seg) o imagen con educación médica |
| Propósito | Mantener el nombre del Dr. Rosas presente — no se espera leads directos |
| Pausa posible | Puede pausarse si el presupuesto es limitado el primer mes |

---

## 2. CÓMO CREAR LAS AUDIENCIAS

### En Meta Business Manager → Audiencias → Crear audiencia → Audiencia personalizada

**Audiencia 1: Visitantes web — 30 días**
- Fuente: Sitio web
- Evento: Todos los visitantes del sitio web
- Período: 30 días
- Nombre: `Visitantes web 30d`

**Audiencia 2: Visitantes web — 60 días**
- Igual pero 60 días
- Nombre: `Visitantes web 60d`

**Audiencia 3: Ya agendaron (excluir de adquisición)**
- Fuente: Sitio web
- Evento: `Lead` (clic en WhatsApp)
- Período: 180 días
- Nombre: `Ya agendaron — Excluir`
- **Esta es la más importante para no desperdiciar dinero**

**Audiencia 4: Interactúan con Instagram/Facebook**
- Fuente: Cuenta de Instagram / Página de Facebook
- Evento: Cualquier interacción (like, comentario, mensaje, guardar)
- Período: 365 días
- Nombre: `Engagers IG/FB 365d`

### Audiencias similares (Lookalike) — crear después de tener 100+ eventos Lead

**Lookalike 1% desde Visitantes web** → más preciso, menor alcance
**Lookalike 1% desde Ya agendaron** → mejor calidad, usar en Campaña 1 cuando tengas datos

> Meta necesita mínimo 100 personas en la Custom Audience para crear un Lookalike confiable.
> Con el pixel activo, en 30-60 días deberías tener suficiente base.

---

## 3. CÓMO ORGANIZAR LOS ANUNCIOS

### Regla: 2-3 creatividades por ad set, nunca 1

Cada ad set necesita variedad para que Meta pruebe y encuentre cuál funciona:

```
Ad Set 1A — Vesícula
├── Anuncio A: Imagen estática — síntoma (cólico biliar)
├── Anuncio B: Video corto 15 seg — testimonial o educativo
└── Anuncio C: Carrusel — 3 beneficios del procedimiento
```

Después de 7-10 días, Meta muestra más presupuesto al que tenga mejor CTR y menor CPL.

---

## 4. PRESUPUESTO RECOMENDADO

### Mes 1-2 (fase de aprendizaje): $8,000 MXN/mes

| Campaña | Presupuesto diario | Mensual |
|---------|--------------------|---------|
| Conversiones — Captación | $160 MXN/día | $4,800 MXN |
| Remarketing | $67 MXN/día | $2,000 MXN |
| Reconocimiento local | $40 MXN/día | $1,200 MXN |
| **Total** | **$267/día** | **$8,000 MXN** |

> Divide los $4,800 de Captación entre los 3 ad sets: $1,600 MXN/mes cada uno (~$53/día).
> Mínimo necesario por ad set para que Meta aprenda: $1,500 MXN/mes.

### Mes 3+ (escalada): $12,000-15,000 MXN/mes

Solo escala los ad sets que estén por debajo de $300 MXN CPL.
Pausa los que superen ese umbral después de 2 semanas.

### ROI esperado con estos números

| Métrica | Estimado |
|---------|---------|
| CPL objetivo | < $300 MXN |
| Leads mes 1 | 15-25 leads |
| Tasa lead → consulta | 30% → 5-8 consultas |
| Tasa consulta → cirugía | 50% → 2-4 cirugías |
| Ingreso promedio por cirugía | $35,000 MXN |
| Ingreso generado | $70,000-140,000 MXN |
| Inversión en ads | $8,000 MXN |
| **ROI mínimo esperado** | **8:1** |

---

## 5. COPIES POR PROCEDIMIENTO

> Meta prohíbe imágenes de cirugías activas, sangre, campos quirúrgicos y antes/después de procedimientos.
> Todos los copies siguientes son compatibles con la política de Meta Healthcare.

---

### VESÍCULA

**Copy 1 — Síntoma directo (mujeres 30-55)**
```
¿Te diagnosticaron cálculos en la vesícula?

Muchas pacientes esperan meses sin necesidad.

La colecistectomía laparoscópica tiene:
✓ Recuperación en 3-5 días
✓ 3 pequeñas incisiones (sin cicatriz visible)
✓ Alta el mismo día o día siguiente

Disponibilidad esta semana en La Paz BCS.

👨‍⚕️ Dr. Alben Rosas — Cirujano General, Cédula 11017193
📲 Escríbeme al WhatsApp para tu valoración
```
**Imagen:** Foto del Dr. Rosas en bata blanca, fondo crema. Sin quirófano.

---

**Copy 2 — Dolor post-comida (mujeres 35-60)**
```
Dolor en el estómago después de comer grasoso o pesado…

No es solo "mala digestión".

Puede ser tu vesícula.

Una valoración con un cirujano te da el diagnóstico en una sola cita —
sin listas de espera, sin rodeos.

📍 Consultorio en La Paz BCS — Médica del Cortés
📲 Agenda hoy por WhatsApp
```

---

### HERNIAS

**Copy 1 — Bulto inguinal (hombres 35-60)**
```
Ese bulto que aparece cuando te agachas o haces fuerza…

No desaparece solo.

Es una hernia — y tiene solución definitiva.

Con técnica laparoscópica:
✓ Sin malla visible ni cicatriz grande
✓ Regresas al trabajo en 7 días
✓ Anestesia general, procedimiento de 45 min

¿Cuánto tiempo llevas aguantando ese dolor?

👨‍⚕️ Dr. Alben Rosas — Cirujano General
📲 Escríbeme y lo resolvemos esta semana
```

---

**Copy 2 — Hernia umbilical (mixto)**
```
Hernia umbilical: ese "ombligo salido" que te preocupa

Es más común de lo que crees, y tiene solución directa.

Cirugía laparoscópica ambulatoria — la mayoría de los pacientes
se van a casa el mismo día.

📍 La Paz BCS / Los Cabos
📲 Consulta de valoración sin compromiso
```

---

### DOLOR ABDOMINAL

**Copy — Valoración general (mixto 30-60)**
```
¿Dolor en el abdomen que lleva semanas sin explicación?

Puede ser:
→ Vesícula con cálculos
→ Hernia incipiente
→ Patología intestinal

Una consulta con un cirujano general te da claridad.
Sin esperas. Sin listas. Diagnóstico directo.

📍 Médica del Cortés, La Paz BCS
📲 Agenda tu valoración hoy
```

---

### APENDICITIS

**Copy — Urgencia / reconocimiento de síntomas**
```
Dolor intenso en el lado derecho inferior del abdomen

Si va acompañado de fiebre, náusea y empeora al moverse —
no esperes.

Puede ser el apéndice.

Cirugía laparoscópica disponible.
Atención de urgencia.

📲 WhatsApp: +52 663 437 0584
```
> Este copy se usa principalmente en campaña de reconocimiento o en remarketing.
> No es para campaña de conversión fría — la apendicitis es urgencia, los pacientes no "comparan opciones".

---

### REMARKETING (visitantes que no agendaron)

**Copy — Segunda oportunidad**
```
Visitaste mi página hace unos días...

Todavía hay lugar esta semana.

Si tienes dudas sobre tu diagnóstico o quieres una segunda opinión —
una valoración contigo toma 30 minutos y te da un plan claro.

📲 Escríbeme hoy, respondo en menos de 2 horas.
— Dr. Alben Rosas
```

---

## 6. MEDIR CONVERSIONES Y ROI CORRECTAMENTE

### Métricas primarias en Meta Ads Manager

| Métrica | Qué mide | Objetivo |
|---------|---------|---------|
| CPL (Costo por Lead) | Costo por clic en WhatsApp | < $300 MXN |
| CTR (Link) | % que hace clic en tu anuncio | > 1.5% |
| Frecuencia | Veces que la misma persona ve el anuncio | < 3 en 7 días |
| Alcance único | Personas distintas que vieron el anuncio | Monitor semanal |

### Métricas de negocio (llevas tú, no Meta)

Crea una hoja de cálculo simple:

| Semana | Leads WhatsApp | Consultas agendadas | Cirugías realizadas | Ingreso |
|--------|---------------|--------------------|--------------------|---------|
| S1 | 8 | 3 | 1 | $35,000 |
| S2 | 12 | 4 | 2 | $70,000 |

Pregunta siempre a los nuevos pacientes: **"¿Cómo nos encontraste?"**
Las respuestas "por Meta / Facebook / Instagram" son tu tracking manual.

### Cálculo de ROI real

```
ROI = (Ingreso generado por pacientes de Meta) ÷ (Gasto en Meta Ads)

Ejemplo:
- Gasto mes: $8,000 MXN
- 3 cirugías atr ibuidas a Meta × $35,000 = $105,000 MXN
- ROI = 105,000 / 8,000 = 13:1
```

### Cuándo escalar

- ROI > 5:1 consistente por 3 semanas → aumenta presupuesto 20%
- CPL < $200 MXN → ese ad set está funcionando muy bien, duplícalo
- CPL > $500 MXN después de 2 semanas → pausa y reformula el copy

---

## 7. REGLAS PARA NO DESPERDICIAR DINERO

### Las 8 reglas de oro

**1. Siempre excluir a personas que ya convirtieron**
→ Agrega "Ya agendaron — Excluir" como exclusión en TODOS los ad sets de Campaña 1.
→ Sin esto, pagas para mostrarle anuncios a alguien que ya es tu paciente.

**2. No toques los ad sets durante los primeros 7 días**
→ Meta está en "fase de aprendizaje" — cada cambio reinicia el algoritmo.
→ La tentación de pausar o ajustar en el día 2 es la razón #1 de campañas fallidas.

**3. Regla del 3x — matar ad sets que no convierten**
→ Si gastaste 3× tu CPL objetivo ($900 MXN) sin un solo Lead → pausa ese ad set.
→ Reformula el copy o la audiencia antes de reactivarlo.

**4. Mínimo 3 creatividades por ad set**
→ Un solo anuncio = Meta no tiene con qué optimizar.
→ 3 anuncios = Meta prueba automáticamente cuál funciona mejor.

**5. Renovar creatividades cada 4-6 semanas**
→ Frecuencia > 3.5 en 7 días = fatiga de anuncio = CPL sube.
→ Señal: CTR cae, CPL sube. Acción: nuevas imágenes/copies.

**6. No usar Audience Network**
→ El tráfico de Audience Network (apps de terceros) es de baja calidad para servicios médicos.
→ Siempre seleccionar ubicaciones manualmente: Feed + Reels/Stories solamente.

**7. No escalar más del 20% por semana**
→ Duplicar el presupuesto de golpe reinicia la fase de aprendizaje.
→ Aumenta máximo 20% cada 5-7 días.

**8. Presupuesto mínimo por ad set**
→ Menos de $50 MXN/día por ad set = Meta no puede optimizar.
→ Si el presupuesto es pequeño, mejor 2 ad sets bien capitalizados que 5 ad sets anémicos.

---

## RESUMEN — Checklist de lanzamiento

```
ANTES DE LANZAR:
[ ] Pixel instalado y verificado — Lead funcionando         ✅ Hecho
[ ] Dominio verificado en Meta                              ✅ Hecho
[ ] Aggregated Event Measurement configurado (Lead prioridad 1)
[ ] Audiencia "Ya agendaron — Excluir" creada
[ ] Audiencia "Visitantes web 60d" creada
[ ] 3 creatividades listas por ad set
[ ] Landing page (dralbenrosas.com) cargando en < 3 seg en móvil

AL LANZAR:
[ ] Campaña 1: Conversiones — 3 ad sets activos
[ ] Campaña 2: Remarketing — activa con exclusión
[ ] Campaña 3: Reconocimiento — opcional mes 1

SEMANA 1 (no tocar nada, solo monitorear):
[ ] CTR > 0.5% (si no, el copy o la imagen no están enganchando)
[ ] Frecuencia < 2 después de 7 días
[ ] Al menos 5-10 leads en la primera semana con $8,000/mes

SEMANA 2-3 (primera optimización):
[ ] Pausar anuncios con CTR < 0.5%
[ ] Pausar ad sets con CPL > $500 MXN
[ ] Escalar ad sets con CPL < $200 MXN (+20% presupuesto)
```

---

## PRÓXIMOS PASOS INMEDIATOS

| Acción | Tiempo | Quién |
|--------|--------|-------|
| Crear las 4 Custom Audiences en Meta | 10 min | Tú |
| Configurar Aggregated Event Measurement (Lead = prioridad 1) | 5 min | Tú |
| Preparar 3 creatividades para Campaña 1 (imágenes + copies) | 30 min | Yo te ayudo |
| Lanzar Campaña 1 y 2 | 20 min | Tú en Meta Ads Manager |

---

*Pixel: 3456701621158975 | Business: 2482834265523958 | GTM: GTM-PXWFLFT5*
