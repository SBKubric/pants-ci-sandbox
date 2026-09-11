"""Юнит-тесты для svc_beta.beta."""

from svc_beta.beta import count_items, has_items, summarize, lightest_weight


def test_summarize() -> None:
    """Сводка содержит количество и суммарный вес сущностей."""
    assert summarize() == "beta: 1 items, total weight 0.5"


def test_count_items() -> None:
    """Количество сущностей в тестовом наборе равно единице."""
    assert count_items() == 1


def test_has_items() -> None:
    """В тестовом наборе есть сущности."""
    assert has_items() is True


def test_lightest_weight() -> None:
    """Самая лёгкая сущность набора beta весит 0.25."""
    assert lightest_weight() == 0.25
