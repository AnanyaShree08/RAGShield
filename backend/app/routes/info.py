from fastapi import APIRouter, Depends

from app.config.setting import Settings
from app.dependencies import get_settings

router = APIRouter(tags=["info"])


@router.get("/info")
async def get_info(config: Settings = Depends(get_settings)):
    return {"name": config.app_name, "version": config.app_version}