from typing import List
from django.core.cache import cache
from .models import Product


def get_products_by_category(category_id: int) -> List[Product]:
    """
    Возвращает список всех продуктов в указанной категории.
    Использует низкоуровневое кеширование с ключом category_{id}.
    Время жизни кеша — 300 секунд (5 минут).
    """
    cache_key = f'category_{category_id}'

    products = cache.get_or_set(
        cache_key,
        lambda: list(Product.objects.filter(category_id=category_id).select_related('category')),
        timeout=300,
    )
    return products
