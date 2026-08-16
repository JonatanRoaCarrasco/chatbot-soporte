from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.tenant import Tenant
from app.schemas.schemas import TenantCreate, TenantResponse

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/tenants", response_model=List[TenantResponse])
def get_tenants(db: Session = Depends(get_db)):
    tenants = db.query(Tenant).all()
    return tenants

@router.post("/tenants", response_model=TenantResponse)
def create_tenant(tenant: TenantCreate, db: Session = Depends(get_db)):
    db_tenant = db.query(Tenant).filter(Tenant.domain == tenant.domain).first()
    if db_tenant:
        raise HTTPException(status_code=400, detail="Domain already registered")
    
    new_tenant = Tenant(**tenant.dict())
    db.add(new_tenant)
    db.commit()
    db.refresh(new_tenant)
    return new_tenant

@router.get("/tenants/{tenant_id}", response_model=TenantResponse)
def get_tenant(tenant_id: int, db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant
