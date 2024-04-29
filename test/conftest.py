import pytest


@pytest.fixture(scope="session")
def celery_config():
    return {"broker_url": "pyamqp://", "result_backend": "rpc://"}


# pytest_plugins = ("celery.contrib.pytest",)


# @pytest.fixture(scope="session")
# def celery_enable_logging():
#     return True


# @pytest.fixture(scope="session")
# def celery_includes():
#     return ["src.celery_tasks"]


# @pytest.fixture(scope="session")
# def celery_config():
#     return {
#         "broker_url": "amqp://",
#         "result_backend": "redis://",
#         "imports": [
#             "src.celery_tasks",
#         ],
#         "task_always_eager": True,
#     }
