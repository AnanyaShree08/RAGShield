FAKE_ITEMS = {1: "apple", 2: "banana"}


def find_item_by_id(item_id: int):
    return FAKE_ITEMS.get(item_id)