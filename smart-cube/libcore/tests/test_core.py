"""Юнит-тесты для libcore.core."""

from libcore.core import Item, total_weight


def test_total_weight() -> None:
    """Сумма весов считается корректно."""
    items = [Item(name="a", weight=1.5), Item(name="b", weight=2.5)]
    assert total_weight(items) == 4.0


def test_total_weight_empty() -> None:
    """Пустой список даёт нулевой суммарный вес."""
    assert total_weight([]) == 0.0
