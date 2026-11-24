from fastapi import APIRouter
from app.schemas.health import HealthResponse
import logging 

logger= logging.getLogger(__name__)

router = APIRouter(tags=["health"])

@router.get("/health" ,response_model=HealthResponse)
async def health_check():
    logger.debug("Health check called")
    logger.info("Health check OK")
    return {"status": "ok"}