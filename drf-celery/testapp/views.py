from django.http import HttpResponse
from django.views import View

from .tasks import test_task


class TestTaskView(View):
    def get(self, request, *args, **kwargs):
        test_task.delay()
        return HttpResponse("Celery task has been triggered")
