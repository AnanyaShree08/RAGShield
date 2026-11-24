from fastapi import HTTPException

from app.repositories.item_repository import find_item_by_id


def get_item_or_404(item_id: int):
    name = find_item_by_id(item_id)
    if name is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, "name": name}