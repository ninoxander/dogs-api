from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import CaracteristicaRaza

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/caracteristicas/")
def read_caracteristicas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(CaracteristicaRaza).offset(skip).limit(limit).all()

@router.get("/caracteristicas/{id_caracteristica}")
def read_caracteristica(id_caracteristica: int, db: Session = Depends(get_db)):
    item = db.query(CaracteristicaRaza).filter(CaracteristicaRaza.id_caracteristica == id_caracteristica).first()
    if not item:
        raise HTTPException(status_code=404, detail="Característica no encontrada")
    return item
