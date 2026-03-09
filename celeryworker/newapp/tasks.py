from celery import shared_task

@shared_task
def task1():
    return 5+5

@shared_task
def task2() :
    return "Im Said..."
