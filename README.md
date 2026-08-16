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

### Prerrequisitos
- Python 3.11+
- Node.js 18+
- Docker (opcional pero recomendado)

### Backend

1. Clonar el repositorio:
```bash
git clone https://github.com/JonatanRoaCarrasco/chatbot-soporte.git
cd chatbot-soporte/backend
```

2. Crear entorno virtual e instalar dependencias:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

3. Ejecutar el servidor:
```bash
uvicorn app.main:app --reload --port 8000
```

4. Abrir en el navegador:
- API: http://127.0.0.1:8000
- Documentación: http://127.0.0.1:8000/docs

### Frontend

1. Ir a la carpeta frontend:
```bash
cd ../frontend
```

2. Instalar dependencias:
```bash
npm install
```

3. Ejecutar en desarrollo:
```bash
npm run dev
```

### Con Docker (recomendado)

1. Instalar Docker Desktop
2. Ejecutar desde la raíz del proyecto:
```bash
docker-compose up
```

Esto levantará:
- Backend en http://localhost:8000
- PostgreSQL en http://localhost:5432
- Redis en http://localhost:6379

## Integrantes del equipo

- Jonatan Roa     - Product Owner
- Nelson Maureira - Scrum Master  
- Daniel Rioseco  - Developer


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
