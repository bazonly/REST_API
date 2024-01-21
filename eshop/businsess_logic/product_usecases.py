from typing import Optional, List

from eshop.businsess_logic.product import Product
from eshop.data_access.product_repo import save, get_by_id, get_many, delete_by_id



def product_create(dto: object) -> Product:
    save(dto)
    return dto

def product_delete(id: str):
    delete_by_id(id)


def product_get_by_id(id: str) -> Optional[Product]:
    return get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    return get_many(page=page, limit=limit)