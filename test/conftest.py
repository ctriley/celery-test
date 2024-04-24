import pytest


@pytest.fixture(scope="session")
def celery_enable_logging():
    return True


@pytest.fixture(scope="session")
def celery_includes():
    return ["src.celery_tasks"]
