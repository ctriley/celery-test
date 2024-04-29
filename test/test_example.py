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


def test_multiply_delay(celery_app, celery_worker) -> None:
    assert src.celery_tasks.multiply.delay(4, 5).get(timeout=10) == 20


def test_multiply(celery_config, celery_worker):
    assert src.celery_tasks.multiply(4, 5) == 20


def test_hellothenmultiply(celery_app, celery_worker):
    assert src.celery_tasks.hellothenmultiply(4, 5).get(timeout=10) == 20
