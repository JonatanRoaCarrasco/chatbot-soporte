from fastapi import APIRouter
from app.api.auth import router as auth_router
from app.api.chat import router as chat_router
from app.api.admin import router as admin_router
from app.api.tickets import router as tickets_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(chat_router)
api_router.include_router(admin_router)
api_router.include_router(tickets_router)
