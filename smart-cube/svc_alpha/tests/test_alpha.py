"""Юнит-тесты для svc_alpha.alpha."""

from svc_alpha.alpha import describe


def test_describe() -> None:
    """Описание содержит количество и суммарный вес сущностей."""
    assert describe() == "alpha: 2 items, total weight 3.0"
