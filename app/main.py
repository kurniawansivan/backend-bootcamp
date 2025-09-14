from fastapi import FastAPI
from app.core.logging import configure_logging
from app.core.settings import settings
from app.api.routes.health import router as health_router
from app.api.routes.products import router as products_router

configure_logging()
app = FastAPI(title=settings.app_name, version=settings.app_version)
app.include_router(health_router)
app.include_router(products_router)
