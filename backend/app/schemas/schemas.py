from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Tenant schemas
class TenantBase(BaseModel):
    name: str
    domain: str
    logo_url: Optional[str] = None

class TenantCreate(TenantBase):
    pass

class TenantResponse(TenantBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# User schemas
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    tenant_id: int
    role: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Chat schemas
class ChatMessageBase(BaseModel):
    content: str

class ChatMessageCreate(ChatMessageBase):
    pass

class ChatMessageResponse(ChatMessageBase):
    id: int
    role: str
    timestamp: datetime
    
    class Config:
        from_attributes = True

class ChatSessionResponse(BaseModel):
    id: int
    tenant_id: int
    channel: str
    status: str
    created_at: datetime
    messages: List[ChatMessageResponse] = []
    
    class Config:
        from_attributes = True
