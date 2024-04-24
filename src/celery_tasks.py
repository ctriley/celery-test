from celery import Celery

app = Celery("hello", broker="amqp://guest@localhost//")


@app.task
def hellothenmultiply(x, y):
    print("hello")
    return multiply.delay(x, y)


@app.task
def multiply(x, y):
    return x * y
