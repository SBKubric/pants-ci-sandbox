"""Юнит-тесты для svc_alpha.alpha."""

from svc_alpha.alpha import count_items, describe, has_items, is_empty


def test_describe() -> None:
    """Описание содержит количество и суммарный вес сущностей."""
    assert describe() == "alpha: 2 items, total weight 3.0"


def test_count_items() -> None:
    """Количество сущностей в тестовом наборе равно двум."""
    assert count_items() == 2


def test_has_items() -> None:
    """В тестовом наборе есть сущности."""
    assert has_items() is True


def test_is_empty() -> None:
    """Тестовый набор непуст."""
    assert is_empty() is False
