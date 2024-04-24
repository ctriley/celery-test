import src.celery_tasks

# pytest_plugins: list[str] = ["celery.contrib.pytest"]


# this fails -- why?
def test_multiply_delay(celery_session_worker) -> None:
    assert src.celery_tasks.multiply.delay(4, 5).get(timeout=10) == 20


def test_multiply(celery_session_worker):
    assert src.celery_tasks.multiply(4, 5) == 20


# this fails as well
def test_hellothenmultiply(celery_session_worker):
    assert src.celery_tasks.hellothenmultiply(4, 5).get(10) == 20
