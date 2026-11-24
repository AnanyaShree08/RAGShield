from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["items"])

FAKE_ITEMS = {1: "apple", 2: "banana"}


@router.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id not in FAKE_ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, "name": FAKE_ITEMS[item_id]}