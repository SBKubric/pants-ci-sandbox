"""Сервис alpha: пример использования общей библиотеки libcore."""

from libcore.core import Item, total_weight


def describe() -> str:
    """Собрать читаемое описание тестового набора сущностей сервиса alpha."""
    items = [Item(name="alpha-1", weight=1.0), Item(name="alpha-2", weight=2.0)]
    return f"alpha: {len(items)} items, total weight {total_weight(items)}"


def count_items() -> int:
    """Вернуть количество сущностей в тестовом наборе сервиса alpha."""
    items = [Item(name="alpha-1", weight=1.0), Item(name="alpha-2", weight=2.0)]
    return len(items)
