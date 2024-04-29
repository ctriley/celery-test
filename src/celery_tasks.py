from .celery_app import app


@app.task
def hellothenmultiply(x, y):
    print("hello")
    return multiply.delay(x, y)


@app.task
def multiply(x, y):
    print("multiply")
    return x * y
