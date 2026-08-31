"""Мок «тяжёлого» интеграционного теста сервиса alpha.

В реальном сервисе здесь были бы testcontainers (PostgreSQL/Redis/RabbitMQ)
и проверки живых gRPC/HTTP серверов. Для песочницы достаточно имитировать
заметную длительность через time.sleep — так в CI видно, что heavy-прогон
действительно исполнялся отдельно от юнит-тестов, а не просто пропущен.
"""

import time

from svc_alpha.alpha import describe


def test_alpha_heavy_roundtrip() -> None:
    """Имитация «тяжёлой» проверки живого внешнего сервиса."""
    time.sleep(1)
    assert describe() != ""
