from django.http import HttpResponse

def celery_test(request):
    from .tasks import test_task

    test_task.delay()
    return HttpResponse("Celery test task has been queued.")