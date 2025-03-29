from typing import List, Optional
from app.models.item_model import Item, ItemCreate
from app.repositories.item_repository import ItemRepository

class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository
    
    def create_item(self, item: ItemCreate) -> Item:
        return self.repository.create(item)
    
    def get_items(self) -> List[Item]:
        return self.repository.get_all()
    
    def get_item(self, item_id: str) -> Optional[Item]:
        return self.repository.get_by_id(item_id)
    
    def update_item(self, item_id: str, item: ItemCreate) -> Optional[Item]:
        return self.repository.update(item_id, item)
    
    def delete_item(self, item_id: str) -> bool:
        return self.repository.delete(item_id)