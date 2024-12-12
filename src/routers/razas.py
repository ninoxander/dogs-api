from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Razas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/razas/")
def read_razas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Obtiene una lista de razas con soporte para paginación."""
    return db.query(Razas).offset(skip).limit(limit).all()

@router.get("/razas/{id_raza}")
def read_raza(id_raza: int, db: Session = Depends(get_db)):
    """Obtiene una raza específica por su ID."""
    item = db.query(Razas).filter(Razas.id_raza == id_raza).first()
    if not item:
        raise HTTPException(status_code=404, detail="Raza no encontrada")
    return item