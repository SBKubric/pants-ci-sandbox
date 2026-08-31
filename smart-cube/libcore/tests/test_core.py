"""Юнит-тесты для libcore.core."""

from libcore.core import Item, average_weight, total_weight


def test_total_weight() -> None:
    """Сумма весов считается корректно."""
    items = [Item(name="a", weight=1.5), Item(name="b", weight=2.5)]
    assert total_weight(items) == 4.0


def test_total_weight_empty() -> None:
    """Пустой список даёт нулевой суммарный вес."""
    assert total_weight([]) == 0.0


def test_average_weight() -> None:
    """Средний вес считается корректно."""
    items = [Item(name="a", weight=1.5), Item(name="b", weight=2.5)]
    assert average_weight(items) == 2.0


def test_average_weight_empty() -> None:
    """Пустой список даёт нулевой средний вес."""
    assert average_weight([]) == 0.0
