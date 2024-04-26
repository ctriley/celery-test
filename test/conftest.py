import pytest


@pytest.fixture(scope="session")
def celery_enable_logging():
    return True


@pytest.fixture(scope="session")
def celery_includes():
    return ["src.celery_tasks"]


@pytest.fixture(scope="session")
def celery_config():
    return {"broker_url": "memory://", "result_backend": "rpc"}
