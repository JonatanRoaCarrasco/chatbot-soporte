from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Chatbot de Soporte Multi-Tenant",
    description="API para plataforma de soporte conversacional",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Chatbot de Soporte API"}

@app.get("/health")
def health():
    return {"status": "ok"}
