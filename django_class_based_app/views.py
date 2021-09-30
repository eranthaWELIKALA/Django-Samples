from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.base import ContextMixin, RedirectView, TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django_class_based_app.models import Course
from django_class_based_app.forms import CourseForm

def is_user_authorized(user):
    return True

decorators = [login_required, user_passes_test(is_user_authorized)]

class DjangoDocumentation(RedirectView):
    url = "https://docs.djangoproject.com/en/3.2/ref/class-based-views/base/"
    

# class IndexView(View):
@method_decorator(decorators, name='dispatch')
class IndexView(TemplateView):
    template_name = "django_class_based_app/course.html"
    context = {}

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    def get(self, request, *args, **kwargs):
        form = CourseForm()
        self.context["form"] = form
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('django_cb_views:course_detail', course.id)
        self.context["form"] = form
        return render(request, self.template_name, self.context)


@method_decorator(login_required, name='dispatch')
class CourseCreateView(CreateView):
    model = Course
    # template_name = ".html"

    def get_success_url(self):
        return reverse_lazy('django_cb_views:course_detail', self.object.id)
 
    # specify the fields to be displayed 
    fields = ['title', 'description']

# In list views 
# This will return the context as below
# context['courses'] = Course.objects.all()
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
    template_name = "django_class_based_app/course_list.html" # This Course List will look for course_list.html by default

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Course List View"
        return context


class CourseNonEmptyListView(ListView):
    queryset = Course.objects.filter(~Q(title=""))
    context_object_name = 'courses'
    template_name = "django_class_based_app/course_list.html" # This Course List will look for course_list.html by default

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Course Non-Empty List View"
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = "django_class_based_app/course_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Course Detail View"
        context["course_detail_list"] = Course.objects.all()
        return context


