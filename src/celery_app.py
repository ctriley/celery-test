from celery import Celery

app = Celery("Hello", backend="rpc://", broker="pyamqp://guest@localhost//")
