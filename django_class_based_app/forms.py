from django import forms
from django_class_based_app.models import Course

class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ("title", "description")
