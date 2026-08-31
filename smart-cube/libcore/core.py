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
