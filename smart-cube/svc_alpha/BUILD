python_sources()

python_tests(
    name="tests",
    sources=["tests/test_alpha.py"],
)

# Heavy-тесты (мок testcontainers/живых сервисов) — отдельный таргет:
# свой tag и batch_compatibility_tag, чтобы CI мог выбрать их отдельно
# от юнит-тестов через --tag=heavy.
python_tests(
    name="tests_heavy",
    sources=["tests/integration/test_alpha_heavy.py"],
    tags=["heavy"],
    batch_compatibility_tag="alpha-heavy",
)
