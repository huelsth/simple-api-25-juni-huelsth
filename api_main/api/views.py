from ninja import NinjaAPI
from .models import Item

api = NinjaAPI()

@api.get("/items")
def list_items(request):
    items = Item.objects.all()
    return [{"id": item.id, "name": item.name, "description": item.description} for item in items]

@api.get("/items/{item_id}")
def get_item(request, item_id: int):
    item = Item.objects.get(id=item_id)
    return {"id": item.id, "name": item.name, "description": item.description}
