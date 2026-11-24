from fastapi import APIRouter

from app.services.item_service import get_item_or_404

router = APIRouter(tags=["items"])


@router.get("/items/{item_id}")
async def get_item(item_id: int):
    return get_item_or_404(item_id)