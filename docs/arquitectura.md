# Arquitectura del Sistema - Chatbot de Soporte Multi-Tenant

## 1. Diagrama de Arquitectura (Alto Nivel)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              FRONTEND                                       │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │   Widget Chat   │  │   Admin Panel   │  │  Agent Console  │            │
│  │   (Embeddable)  │  │   (Multi-tenant)│  │   (Human Agent) │            │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘            │
│           │                    │                    │                      │
└───────────┼────────────────────┼────────────────────┼──────────────────────┘
            │                    │                    │
            ▼                    ▼                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           API GATEWAY (FastAPI)                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ Auth Module │  │ Chat Module │  │ Admin Module│  │Ticket Module│      │
│  │   (JWT)     │  │  (WebSocket)│  │  (CRUD)     │  │  (Corestream)│      │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘      │
└─────────────────────────────────────────────────────────────────────────────┘
            │                    │                    │
            ▼                    ▼                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SERVICIOS                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │  RAG Engine │  │   LLM API   │  │  Embeddings │  │  Ticket API │      │
│  │ (Retrieval) │  │  (DeepSeek) │  │  (Vector)   │  │ (Corestream)│      │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘      │
└─────────────────────────────────────────────────────────────────────────────┘
            │                    │                    │
            ▼                    ▼                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DATA LAYER                                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ PostgreSQL  │  │    Redis    │  │   Vector    │  │   Storage   │      │
│  │  (Primary)  │  │  (Cache)    │  │   (PgVector)│  │  (Files)    │      │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Componentes Detallados

### 2.1 Frontend

| Componente | Tecnología | Función |
|------------|------------|---------|
| **Widget Chat** | Vue 3 / React + TypeScript | Chat embebido en apps cliente, responsive |
| **Admin Panel** | Vue 3 / React + TypeScript | Gestión de tenants, conocimiento, agentes |
| **Agent Console** | Vue 3 / React + TypeScript | Consola para agentes humanos (cola, transcripción) |

### 2.2 Backend (FastAPI)

| Módulo | Función | Endpoints |
|--------|---------|-----------|
| **Auth** | Autenticación JWT, control de acceso por rol y tenant | `/auth/login`, `/auth/register`, `/auth/refresh` |
| **Chat** | Motor conversacional, WebSocket, historial | `/chat/send`, `/chat/history`, `/ws/chat` |
| **Admin** | CRUD de tenants, documentos, FAQ, agentes | `/admin/tenants`, `/admin/documents`, `/admin/faq` |
| **Tickets** | Integración con Corestream | `/tickets/create`, `/tickets/status`, `/tickets/assign` |
| **Knowledge** | Ingesta de documentos, vectorización | `/knowledge/upload`, `/knowledge/search` |

### 2.3 Servicios

| Servicio | Descripción |
|----------|-------------|
| **RAG Engine** | Recupera documentos relevantes para responder consultas |
| **LLM API** | DeepSeek u otro LLM para generar respuestas |
| **Embeddings** | Genera vectores para búsqueda semántica |
| **Ticket API** | Conector con Corestream para gestión de casos |

---

## 3. Modelo de Datos (ER)

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│    tenants      │     │    users        │     │   chat_sessions │
├─────────────────┤     ├─────────────────┤     ├─────────────────┤
│ id (PK)         │────<│ id (PK)         │────<│ id (PK)         │
│ name            │     │ tenant_id (FK)  │     │ tenant_id (FK)  │
│ domain          │     │ email           │     │ user_id (FK)    │
│ logo_url        │     │ role            │     │ channel         │
│ config (JSONB)  │     │ created_at      │     │ status          │
│ created_at      │     └─────────────────┘     │ created_at      │
└─────────────────┘                             └─────────────────┘
        │                                               │
        │                                               │
        ▼                                               ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  documents      │     │     faq         │     │ chat_messages   │
├─────────────────┤     ├─────────────────┤     ├─────────────────┤
│ id (PK)         │     │ id (PK)         │     │ id (PK)         │
│ tenant_id (FK)  │     │ tenant_id (FK)  │     │ session_id (FK) │
│ title           │     │ question        │     │ role            │
│ content         │     │ answer          │     │ content         │
│ type            │     │ category        │     │ timestamp       │
│ chat_type       │     │ created_at      │     │ metadata (JSONB)│
│ embedding       │     └─────────────────┘     └─────────────────┘
│ created_at      │
└─────────────────┘
        │
        ▼
┌─────────────────┐     ┌─────────────────┐
│    agents       │     │    tickets      │
├─────────────────┤     ├─────────────────┤
│ id (PK)         │     │ id (PK)         │
│ tenant_id (FK)  │     │ session_id (FK) │
│ name            │     │ external_id     │
│ type            │     │ status          │
│ config (JSONB)  │     │ priority        │
│ human_agent_id  │     │ assigned_to     │
│ created_at      │     │ created_at      │
└─────────────────┘     └─────────────────┘
```

---

## 4. Flujo de una Conversación

```
Usuario                Widget Chat              API Gateway           RAG Engine
  │                         │                        │                     │
  │  1. Envía mensaje       │                        │                     │
  │────────────────────────>│                        │                     │
  │                         │  2. WebSocket msg      │                     │
  │                         │───────────────────────>│                     │
  │                         │                        │  3. Busca contexto  │
  │                         │                        │────────────────────>│
  │                         │                        │                     │
  │                         │                        │  4. Documentos      │
  │                         │                        │<────────────────────│
  │                         │                        │                     │
  │                         │                        │  5. Genera prompt   │
  │                         │                        │────────────────────>│ (LLM)
  │                         │                        │                     │
  │                         │                        │  6. Respuesta       │
  │                         │                        │<────────────────────│
  │                         │                        │                     │
  │                         │  7. Respuesta          │                     │
  │                         │<───────────────────────│                     │
  │  8. Recibe respuesta    │                        │                     │
  │<────────────────────────│                        │                     │
  │                         │                        │                     │
  │  [Si no resuelve]       │                        │                     │
  │                         │  9. Crear ticket       │                     │
  │                         │───────────────────────>│────> Corestream     │
```

---

## 5. Estructura de Carpetas

```
chatbot-soporte/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   ├── chat.py
│   │   │   ├── admin.py
│   │   │   └── tickets.py
│   │   ├── services/
│   │   │   ├── rag.py
│   │   │   ├── llm.py
│   │   │   └── embeddings.py
│   │   └── core/
│   │       ├── security.py
│   │       └── database.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── services/
│   │   └── main.ts
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── docs/
│   ├── arquitectura.md
│   ├── api.md
│   └── despliegue.md
├── .gitignore
├── README.md
└── Documento_Inicio_Proyecto_Chatbot.md
```

---

## 6. Tecnologías y Justificación

| Capa | Tecnología | Justificación |
|------|------------|---------------|
| **Backend** | Python + FastAPI | Rápido, async, documentación automática (OpenAPI) |
| **Base de datos** | PostgreSQL | Robusto, soporte JSONB para configuración flexible |
| **Cache** | Redis | Sesiones, cola de mensajes, rate limiting |
| **Vectores** | PgVector | Extensión de PostgreSQL, no requiere otro servicio |
| **IA** | DeepSeek API | Modelo de lenguaje potente y económico |
| **Frontend** | Vue 3 / React + TypeScript | Componentes reutilizables, tipado seguro |
| **Tiempo real** | WebSocket | Comunicación bidireccional para chat en vivo |
| **Container** | Docker + Docker Compose | Despliegue consistente, fácil escalabilidad |

---

## 7. Requisitos No Funcionales

| Requisito | Estrategia |
|-----------|------------|
| **Seguridad** | JWT + RBAC, cifrado de API keys, rate limiting |
| **Escalabilidad** | Multi-tenant por diseño, Workers asíncronos |
| **Disponibilidad** | Health checks, supervisión con Application Insights |
| **Rendimiento** | Redis cache, embeddings pre-calculados, CDN |
| **Mantenibilidad** | Código modular, tests, CI/CD con GitHub Actions |

---

**Estado**: Borrador v1.0  
**Última actualización**: Agosto 2026
