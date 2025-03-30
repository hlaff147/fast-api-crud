from app.services.item_services import ItemService
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from app.models.item_model import Item, ItemCreate
from app.repositories.item_repository import ItemRepository

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

# Dependency Injection
def get_item_service():
    repository = ItemRepository()
    return ItemService(repository)

@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate, service: ItemService = Depends(get_item_service)):
    """Create a new item"""
    return service.create_item(item)

@router.get("/", response_model=List[Item])
async def read_items(service: ItemService = Depends(get_item_service)):
    """Get all items"""
    return service.get_items()

@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: str, service: ItemService = Depends(get_item_service)):
    """Get a specific item by ID"""
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: str, item: ItemCreate, service: ItemService = Depends(get_item_service)):
    """Update an item"""
    updated_item = service.update_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, service: ItemService = Depends(get_item_service)):
    """Delete an item"""
    success = service.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return None
