"""Юнит-тесты для libcore.core."""

from libcore.core import Item, average_weight, max_weight, min_weight, total_weight


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


def test_max_weight() -> None:
    """Максимальный вес находится корректно."""
    items = [Item(name="a", weight=1.5), Item(name="b", weight=2.5)]
    assert max_weight(items) == 2.5


def test_max_weight_empty() -> None:
    """Пустой список даёт нулевой максимальный вес."""
    assert max_weight([]) == 0.0


def test_min_weight() -> None:
    """Минимальный вес находится корректно."""
    items = [Item(name="a", weight=1.5), Item(name="b", weight=2.5)]
    assert min_weight(items) == 1.5


def test_min_weight_empty() -> None:
    """Пустой список даёт нулевой минимальный вес."""
    assert min_weight([]) == 0.0
