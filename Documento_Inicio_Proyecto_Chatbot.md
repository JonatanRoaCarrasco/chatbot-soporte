# Documento de Inicio de Proyecto CAPSTONE

## Chatbot de Soporte Multi-Tenant

---

## 1. Problema u Oportunidad

Cada producto SaaS del ecosistema (WellQ, Alloxentric, Dani ETH, Dani27001, Aprueba) necesita atender consultas y problemas de sus usuarios finales. Actualmente, hacerlo con soporte humano dedicado por producto es **costoso y no escala**.

El soporte humano implica:
- Contratar personal capacitado por cada producto
- Mantener horarios de atención extendidos
- Responder preguntas repetitivas que un bot podría resolver
- Gestionar múltiples canales de comunicación por separado

**Oportunidad**: Crear una primera línea de atención automatizada y compartida mediante un bot conversacional capaz de responder preguntas frecuentes y, cuando no puede resolver, registrar el caso como ticket en una ticketera común, de modo que un mismo mecanismo de soporte sirva a múltiples productos.

---

## 2. Objetivos del Proyecto

### Objetivo General
Desarrollar una plataforma multi-tenant de soporte conversacional que permita a múltiples productos SaaS ofrecer atención automatizada a sus usuarios mediante un bot con IA, integrado con una ticketera genérica para escalamiento a soporte humano.

### Objetivos Específicos
1. Desarrollar un motor conversacional basado en RAG (Retrieval-Augmented Generation) que responda consultas a partir de la documentación de cada producto
2. Implementar un sistema multi-tenant que permita configurar bases de conocimiento, reglas de escalamiento y personalización por cada SaaS atendido
3. Integrar una ticketera genérica (Corestream) para la gestión de casos que excedan la capacidad del bot
4. Crear un widget de chat embebible que se integre en las aplicaciones de cada producto
5. Desarrollar un módulo de administración para gestión de tenants, bases de conocimiento y métricas

---

## 3. Usuarios o Stakeholders

| Stakeholder | Rol | Necesidades |
|-------------|-----|-------------|
| **Usuarios finales** | Consultan soporte de los SaaS | Respuestas rápidas, 24/7, en su idioma |
| **Equipos de soporte humano** | Atienden casos derivados del bot | Tickets organizados, contexto de la conversación, herramientas de gestión |
| **Administradores de plataforma** | Configuran tenants y reglas | Panel de administración, métricas de uso, gestión de conocimiento |
| **Clientes SaaS** (WellQ, Alloxentric, Dani, etc.) | Consumen el servicio de soporte | Configuración sencilla, personalización, reportes de atención |

---

## 4. Alcance del MVP

### Dentro del alcance
- Motor conversacional con RAG y clasificación de intención
- Widget de chat web embebible
- Integración con ticketera genérica (Corestream)
- Módulo de administración multi-tenant
- Soporte multi-idioma (español, inglés, portugués)
- Paneles básicos de métricas

### Fuera del alcance (primera versión)
- Derivación a agentes humanos por WhatsApp
- Canales adicionales (telefonía, Telegram, redes sociales)
- Facturación automática a clientes
- App móvil dedicada

---

## 5. Restricciones

| Restricción | Descripción |
|-------------|-------------|
| **Tiempo** | 1 semestre académico (~18 semanas) |
| **Equipo** | 3 integrantes |
| **Tecnología** | Python/FastAPI, PostgreSQL, Redis, SPA moderna |
| **Infraestructura** | Debe ser desplegable en la nube |
| **Documentación** | Repositorio público en GitHub con README obligatorio |

---

## 6. Justificación de la Solución

### ¿Por qué esta solución?

1. **Reducción de costos**: Un bot puede atender múltiples productos simultáneamente, eliminando la necesidad de soporte humano dedicado por SaaS

2. **Escalabilidad**: La arquitectura multi-tenant permite incorporar nuevos productos sin desarrollo adicional significativo

3. **Disponibilidad 24/7**: El bot ofrece atención continua, mejorando la experiencia del usuario

4. **Integración existente**: Aprovecha la infraestructura de Corestream (ticketera) y el ecosistema de tecnologías ya utilizado por los productos del grupo

5. **Diferenciación**: Un soporte con IA que aprende de la documentación específica de cada producto ofrece respuestas más precisas que un chatbot genérico

### Stack Tecnológico Propuesto

| Capa | Tecnología |
|------|------------|
| Backend / API | Python con FastAPI |
| Base de datos | PostgreSQL + Redis |
| Motor de IA | LLM con RAG (DeepSeek u otro) |
| Frontend | Vue 3 o React con TypeScript |
| Ticketera | Integración con Corestream |
| Tiempo real | WebSockets |

---

## 7. Metodología de Trabajo

**Metodología seleccionada**: Scrum

**Duración de sprints**: 2 semanas

**Ceremonias**:
- **Sprint Planning** (inicio de cada sprint): definir objetivos y tareas
- **Daily Scrum** (diario, 15 min): avances, bloqueos, plan del día
- **Sprint Review** (fin de sprint): demo del avance al equipo
- **Sprint Retrospective** (fin de sprint): qué mejorar en el proceso

**Roles**:
- **Product Owner** (Jonatan Roa): prioriza el backlog, representa las necesidades del usuario y del proyecto
- **Scrum Master** (Nelson Maureira): facilita el proceso, quita bloqueos, asegura que se cumplan las ceremonias
- **Developer** (Daniel Rioseco): desarrollo principal del proyecto

**Herramientas**:
- Control de versiones: GitHub (repositorio público)
- Gestión de tareas: GitHub Projects (tablero Kanban vinculado al repositorio)
- Comunicación: Discord (servidor del equipo con canales por tema)

---

## 8. Cronograma Preliminar

| Fase | Semanas | Actividad |
|------|---------|-----------|
| **Fase 1** | 1-4 | Definición del proyecto, diseño de la arquitectura, configuración del entorno |
| **Fase 2** | 5-9 | Desarrollo del motor conversacional, integración con ticketera, módulo de administración |
| **Fase 3** | 10-15 | Desarrollo del widget de chat, pruebas, documentación |
| **Fase 4** | 16-18 | Presentación del proyecto a comisión evaluadora |

---

**Fecha de elaboración**: Agosto 2026  
**Equipo**: Chatbot de Soporte  
**Integrantes**: 
- Jonatan Roa - Product Owner
- Nelson Maureira - Scrum Master
- Daniel Rioseco - Developer
  
**Sección**: CAPSTONE_006V  
**Docente**: ALEX ULISES ZUNIGA MONTIEL
