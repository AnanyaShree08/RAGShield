import logging 
from fastapi import FastAPI
from app.routes.health import router as health_router
from app.config.setting import settings
from app.config.logging_config import setup_logging
from app.routes.items import router as items_router

setup_logging()
logger = logging.getLogger(__name__)
app = FastAPI(title=settings.app_name, version=settings.app_version)
app.include_router(health_router, prefix="/api/v1")
app.include_router(items_router, prefix="/api/v1")

logger.info("%s v%s startingg..",settings.app_name,settings.app_version)
