from django.urls import path
from django_template_tags.views import index, filters, tags

urlpatterns = [
    path('', index, name="index"),
    path('filters/', filters, name="filters"),
    path('tags/', tags, name="tags"),
]
