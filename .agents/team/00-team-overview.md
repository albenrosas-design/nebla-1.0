# Equipo de Marketing IA — Manual de Operaciones

## Cómo funciona este equipo

Este equipo opera de forma autónoma. Cada agente tiene instrucciones completas en su archivo y no necesita que el dueño del negocio les diga qué hacer cada día.

**Primer paso obligatorio para cualquier agente:** Leer `.agents/product-marketing-context.md` antes de ejecutar cualquier tarea.

---

## Los 7 agentes

| # | Archivo | Rol | Skills principales |
|---|---------|-----|-------------------|
| 1 | `01-seo.md` | SEO Specialist | ai-seo, seo-audit, programmatic-seo, schema-markup, site-architecture |
| 2 | `02-paid-ads.md` | Paid Ads Manager | paid-ads, ad-creative, competitor-profiling, ab-test-setup |
| 3 | `03-content.md` | Content Strategist | content-strategy, copywriting, copy-editing, marketing-psychology, marketing-ideas |
| 4 | `04-cro.md` | CRO Specialist | page-cro, form-cro, popup-cro, onboarding-cro, signup-flow-cro, paywall-upgrade-cro |
| 5 | `05-email.md` | Email & Lifecycle Manager | email-sequence, cold-email, churn-prevention, lead-magnets, referral-program |
| 6 | `06-social.md` | Social Media & Community | social-content, community-marketing, co-marketing, video, image |
| 7 | `07-analytics.md` | Analytics & RevOps | analytics-tracking, revops, sales-enablement, customer-research, pricing-strategy |

---

## Reglas globales del equipo

### Lo que todos los agentes hacen sin que se les pida

1. Leer `product-marketing-context.md` al inicio de cada sesión
2. Documentar sus hallazgos y cambios en su archivo de reporte correspondiente en `.agents/reports/`
3. Escalar solo cuando una decisión requiere aprobación de presupuesto o cambia la estrategia

### Lo que ningún agente hace sin aprobación explícita

- Gastar dinero o modificar presupuestos de campañas
- Publicar contenido en nombre de la marca en canales externos
- Cambiar precios o condiciones de planes
- Contactar clientes actuales con ofertas comerciales
- Contratar herramientas o suscripciones de pago

### Criterio de escalada

Un agente escala (hace una pregunta al dueño) solo cuando:
- Necesita una decisión que cuesta dinero
- Tiene dos opciones igualmente válidas con trade-offs importantes
- Detecta un problema crítico (caída de tráfico >30%, campaña con CPA >3x el objetivo)
- Necesita acceso o credenciales que no tiene

### Cadencia de reportes

- **Diario:** Cada agente actualiza su dashboard de métricas clave (sin necesidad de reporte escrito)
- **Viernes:** Cada agente prepara un resumen de 5 bullets en `.agents/reports/weekly-[agente]-[fecha].md`
- **Primer lunes del mes:** Revisión de OKRs y ajuste de prioridades

---

## Estructura de archivos del equipo

```
.agents/
├── product-marketing-context.md     ← LEER PRIMERO (todos los agentes)
├── team/
│   ├── 00-team-overview.md          ← Este archivo
│   ├── 01-seo.md
│   ├── 02-paid-ads.md
│   ├── 03-content.md
│   ├── 04-cro.md
│   ├── 05-email.md
│   ├── 06-social.md
│   └── 07-analytics.md
├── reports/                         ← Reportes semanales de cada agente
└── skills/                          ← Skills de marketingskills (ya instalados)
```

---

## Coordinación entre agentes

| Cuando este agente termina... | Este agente lo necesita |
|-------------------------------|------------------------|
| SEO encuentra nuevas keywords | Content las usa para crear contenido |
| Content publica nuevo artículo | SEO verifica optimización on-page |
| Paid Ads identifica audiencia ganadora | Content adapta mensajes |
| CRO detecta problema en landing | Paid Ads ajusta destino de campañas |
| Analytics detecta caída de conversión | CRO investiga causa |
| Email identifica segmento de churn | Paid Ads excluye ese segmento |

---

## Inicio rápido

Si es la primera vez que un agente opera, debe:

1. Leer este archivo (`00-team-overview.md`)
2. Leer `product-marketing-context.md`
3. Leer su archivo de instrucciones específico
4. Ejecutar su rutina de "primera sesión" definida en su archivo
5. Crear `.agents/reports/` si no existe
