"""Юнит-тесты для svc_beta.beta."""

from svc_beta.beta import summarize


def test_summarize() -> None:
    """Сводка содержит количество и суммарный вес сущностей."""
    assert summarize() == "beta: 1 items, total weight 0.5"
