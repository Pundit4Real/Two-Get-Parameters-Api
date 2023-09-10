from django.urls import re_path as url
from .views import SlackFirstTask


urlpatterns = [
    url(r'api', SlackFirstTask.as_view()),
]