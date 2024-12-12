from sqlalchemy import Column, Integer, String, Enum, Boolean, Text, Float, TIMESTAMP
from database import Base

class CaracteristicaRaza(Base):
    __tablename__ = "caracteristicas_raza"
    id_caracteristica = Column(Integer, primary_key=True, index=True)
    id_raza = Column(Integer)
    nivel_energia = Column(Enum("Bajo", "Medio", "Alto"))
    nivel_entrenabilidad = Column(Enum("Fácil", "Moderado", "Difícil"))
    amigable_ninos = Column(Boolean)
    pelaje = Column(Enum("Corto", "Largo", "Rizado", "Sin pelo"))

class LogsSistema(Base):
    __tablename__ = "logs_sistema"
    id_log = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer)
    accion = Column(String(100))
    descripcion = Column(Text)
    fecha_hora = Column(TIMESTAMP)
    direccion_ip = Column(String(45))

class Razas(Base):
    __tablename__ = "razas"
    id_raza = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    origen = Column(String(100))
    esperanza_vida = Column(Float)
    tamano = Column(Enum("Pequeño", "Mediano", "Grande"))
    peso_min = Column(Float)
    peso_max = Column(Float)
    descripcion = Column(Text)
    fecha_registro = Column(TIMESTAMP)

class RegistrosModificacion(Base):
    __tablename__ = "registros_modificacion"
    id_registro = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer)
    id_raza = Column(Integer)
    tipo_modificacion = Column(Enum("Inserción", "Modificación", "Eliminación"))
    fecha_modificacion = Column(TIMESTAMP)
    detalles_modificacion = Column(Text)

class Usuarios(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    email = Column(String(100))
    contrasena = Column(String(255))
    rol = Column(Enum("Admin", "Usuario"))
    fecha_registro = Column(TIMESTAMP)
    ultimo_acceso = Column(TIMESTAMP)