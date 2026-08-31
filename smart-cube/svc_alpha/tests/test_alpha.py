"""Юнит-тесты для svc_alpha.alpha."""

from svc_alpha.alpha import count_items, describe


def test_describe() -> None:
    """Описание содержит количество и суммарный вес сущностей."""
    assert describe() == "alpha: 2 items, total weight 3.0"


def test_count_items() -> None:
    """Количество сущностей в тестовом наборе равно двум."""
    assert count_items() == 2
