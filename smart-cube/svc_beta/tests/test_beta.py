"""Юнит-тесты для svc_beta.beta."""

from svc_beta.beta import count_items, summarize


def test_summarize() -> None:
    """Сводка содержит количество и суммарный вес сущностей."""
    assert summarize() == "beta: 1 items, total weight 0.5"


def test_count_items() -> None:
    """Количество сущностей в тестовом наборе равно единице."""
    assert count_items() == 1
