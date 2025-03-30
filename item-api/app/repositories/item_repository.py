from typing import Dict, List, Optional
from uuid import uuid4
from app.models.item_model import Item, ItemCreate

class ItemRepository:
    _instance = None
    _items_db: Dict[str, dict] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create(self, item: ItemCreate) -> Item:
        item_id = str(uuid4())
        item_dict = item.dict()
        item_dict["id"] = item_id
        self._items_db[item_id] = item_dict
        return Item(**item_dict)
    
    def get_all(self) -> List[Item]:
        return [Item(**item) for item in self._items_db.values()]
    
    def get_by_id(self, item_id: str) -> Optional[Item]:
        item = self.items_db.get(item_id)
        if item:
            return Item(**item)
        return None
    
    def update(self, item_id: str, item: ItemCreate) -> Optional[Item]:
        if item_id not in self.items_db:
            return None
        
        updated_item = item.dict()
        updated_item["id"] = item_id
        self.items_db[item_id] = updated_item
        return Item(**updated_item)
    
    def delete(self, item_id: str) -> bool:
        if item_id not in self.items_db:
            return False
        
        del self.items_db[item_id]
        return True