import celery
import pytest
import src.celery_tasks
from src.celery_app import app
from typing import Literal
from celery.contrib.pytest import celery_app

# pytest_plugins: list[str] = ["celery.contrib.pytest"]


pytest_plugins: tuple[Literal["celery.contrib.pytest"]] = ("celery.contrib.pytest",)


def test_one(celery_app, celery_worker):
    result = src.celery_tasks.multiply.delay(4, 5).get(timeout=10)
    assert result == 20


# this fails -- why?
# Only works this way
# @pytest.mark.celery(
#     broker_url="redis://localhost:6379", result_backend="redis://localhost:6379"
# )
# # Worker initialized per test
# @pytest.mark.usefixtures("celery_worker")
# def test_multiply_delay() -> None:
#     assert src.celery_tasks.multiply.delay(4, 5).get(timeout=10) == 20


# def test_multiply(celery_config, celery_worker):
#     assert src.celery_tasks.multiply(4, 5) == 20


# # this fails as well
# @pytest.mark.usefixtures("celery_session_app")
# @pytest.mark.usefixtures("celery_session_worker")
# def test_hellothenmultiply(celery_config, celery_session_app, celery_session_worker):
#     assert src.celery_tasks.hellothenmultiply(4, 5).get(timeout=10) == 20
