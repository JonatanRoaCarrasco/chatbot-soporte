# Chatbot de Soporte Multi-Tenant

## Descripción
Plataforma multi-tenant de soporte conversacional que permite a múltiples productos SaaS ofrecer atención automatizada a sus usuarios mediante un bot con IA, integrado con una ticketera genérica para escalamiento a soporte humano.

## Problema que resuelve
Cada producto SaaS del ecosistema necesita atender consultas y problemas de sus usuarios, y hacerlo con soporte humano dedicado por producto es costoso y no escala. Esta solución ofrece una primera línea de atención automatizada y compartida.

## Tecnologías utilizadas
- **Backend**: Python, FastAPI
- **Base de datos**: PostgreSQL, Redis
- **IA**: RAG (Retrieval-Augmented Generation) con LLM
- **Frontend**: Vue 3 / React con TypeScript
- **Ticketera**: Integración con Corestream
- **Control de versiones**: Git, GitHub
- **Gestión de tareas**: GitHub Projects
- **Comunicación**: Discord

## Instrucciones para ejecutar
[Por completar cuando se defina el stack]

## Integrantes del equipo
<<<<<<< HEAD
- Jonatan Roa - Product Owner
- Nelson Maureira - Scrum Master
- Daniel Rioseco - Developer
=======
- Jonatan Roa     - Product Owner
- Nelson Maureira - Scrum Master  
- Daniel Rioseco  - Developer
>>>>>>> 5bfb0971116bcd2dfdd2631419d5a3b04a45f061

## Metodología de trabajo
Scrum con sprints de 2 semanas

## Arquitectura de la solución
Ver documento completo: [docs/arquitectura.md](docs/arquitectura.md)

**Resumen**:
- **Frontend**: Widget Chat (embebible), Admin Panel, Agent Console
- **Backend**: FastAPI con módulos Auth, Chat, Admin, Tickets
- **Servicios**: RAG Engine, LLM (DeepSeek), PgVector
- **Datos**: PostgreSQL (principal), Redis (cache), PgVector (embeddings)
- **Infraestructura**: Docker + Docker Compose
