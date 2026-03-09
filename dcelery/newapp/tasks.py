from celery import shared_task

@shared_task
def sharedTask():
    return

@shared_task
def sharedTask2() :
    return "Im Said..."
