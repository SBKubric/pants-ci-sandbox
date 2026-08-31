"""Общая библиотека: доменная модель, используемая сервисами alpha и beta."""

import attrs


@attrs.frozen
class Item:
    """Простая доменная сущность с именем и весом."""

    name: str
    weight: float = 0.0


def total_weight(items: list[Item]) -> float:
    """Посчитать суммарный вес списка сущностей."""
    return sum(item.weight for item in items)


def average_weight(items: list[Item]) -> float:
    """Посчитать средний вес сущности в списке (0.0 для пустого списка)."""
    if not items:
        return 0.0
    return total_weight(items) / len(items)


def max_weight(items: list[Item]) -> float:
    """Найти максимальный вес сущности в списке (0.0 для пустого списка)."""
    if not items:
        return 0.0
    return max(item.weight for item in items)


def min_weight(items: list[Item]) -> float:
    """Найти минимальный вес сущности в списке (0.0 для пустого списка)."""
    if not items:
        return 0.0
    return min(item.weight for item in items)
