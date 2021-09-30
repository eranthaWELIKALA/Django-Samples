from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'django_template_tags/index.html', {})


def filters(request):
    return render(request, 'django_template_tags/filters.html', {})


def tags(request):
    list_items = ["List Item 01", "List Item 02", "List Item 03", "List Item 04", "List Item 05"]
    return render(request, 'django_template_tags/tags.html', {'list_items': list_items})
