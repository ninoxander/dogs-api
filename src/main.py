from fastapi import FastAPI
from routers import caracteristicas 
from routers import razas

app = FastAPI(
    title="API de Razas de Perros",
    description="Una API para gestionar razas de perros y sus características.",
    version="1.0.0",
    contact={
        "name": "Daniela Ivette Nava Miranda",
        "url": "https://www.linkedin.com/in/nino-dev/",
        "email": "tu_email@example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.include_router(caracteristicas.router, prefix="/api", tags=["Características"])
app.include_router(caracteristicas.router, prefix="/api", tags=["Razas"])