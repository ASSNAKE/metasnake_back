from metasnake.celery import app
from metasnake.apps.data.models import *
from metasnake.apps.data.functions import *
from datetime import datetime


@app.task
def test_task(x, y):
    return x + y
