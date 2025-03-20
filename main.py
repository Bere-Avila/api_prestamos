from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import user
from routes.material import material
from routes.prestamo import prestamo

# Crear la aplicación FastAPI
app = FastAPI(
    title="PRESTAMOS S.A. de C.V.",
    description="API de prueba para almacenar registros de préstamo de material educativo."
)

# Agregar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes. En producción, puedes restringir esto.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Incluir los routers
app.include_router(user)
app.include_router(material)
app.include_router(prestamo)
