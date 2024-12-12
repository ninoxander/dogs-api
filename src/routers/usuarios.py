from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuarios

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/usuarios/")
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Obtiene una lista de usuarios con soporte para paginación."""
    return db.query(Usuarios).offset(skip).limit(limit).all()

@router.get("/usuarios/{id_usuario}")
def read_usuario(id_usuario: int, db: Session = Depends(get_db)):
    """Obtiene un usuario específico por su ID."""
    item = db.query(Usuarios).filter(Usuarios.id_usuario == id_usuario).first()
    if not item:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return item
