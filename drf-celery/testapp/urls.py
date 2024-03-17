from django.urls import path

from .views import TestTaskView

urlpatterns = [
    path("api/celery-test/", TestTaskView.as_view(), name="celery-test"),
]
