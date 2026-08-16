from fastapi import APIRouter

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.get("/")
def get_tickets():
    return {"message": "Tickets endpoint - Corestream integration pending"}

@router.post("/")
def create_ticket():
    return {"message": "Create ticket - Corestream integration pending"}
