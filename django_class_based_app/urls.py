from django.db.models.indexes import Index
from django.urls import path
from django_class_based_app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('create/', CourseCreateView.as_view(), name="course_create"),
    path('course-list/', CourseListView.as_view(), name="course_list"),
    path('course-non-empty-list/', CourseNonEmptyListView.as_view(), name="course_non_empty_list"),
    path('course-detail/<int:pk>/', CourseDetailView.as_view(), name="course_detail" ),
    path('view-doc/', DjangoDocumentation.as_view(), name="django_documentation"),
]
