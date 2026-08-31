"""Сервис beta: пример использования общей библиотеки libcore."""

from libcore.core import Item, total_weight


def summarize() -> str:
    """Собрать сводку по тестовому набору сущностей сервиса beta."""
    items = [Item(name="beta-1", weight=0.5)]
    return f"beta: {len(items)} items, total weight {total_weight(items)}"


def count_items() -> int:
    """Вернуть количество сущностей в тестовом наборе сервиса beta."""
    items = [Item(name="beta-1", weight=0.5)]
    return len(items)


def has_items() -> bool:
    """Есть ли сущности в тестовом наборе сервиса beta."""
    return count_items() > 0
