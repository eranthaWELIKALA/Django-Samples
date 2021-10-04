from django.db.models.indexes import Index
from django.urls import path
from django_send_mails.views import *

urlpatterns = [
    path('', Index.as_view(), name="index"),
]
