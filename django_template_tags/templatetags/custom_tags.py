# This file name doesn't have to be custom_tags
# This filename is the name we are going to use when loading the tags in the template file

from django import template
from django.utils import timezone

register = template.Library()

@register.simple_tag(name="current_time")
def current_time():
    return timezone.now().time()

def get_current_date():
    return timezone.now().date()

@register.simple_tag(takes_context=True)
def separate_by_symbols(context, value, symbol=" | "):    
    if context and value:
        key = str(value)
        if context[key]:
            str_list = list(context[key])
            return symbol.join(str_list)
    return ""    

# Inclusion tags is used to render an HTML component as the result
@register.inclusion_tag(takes_context=True, filename="django_template_tags/components/ul_list.html")
def ul_list(context, value):    
    if context and value:
        key = str(value)
        if context[key]:
            return {'items': context[key]} 
    return ""   


register.simple_tag(get_current_date, name="current_date")
