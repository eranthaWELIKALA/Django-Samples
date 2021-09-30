# This file name doesn't have to be custom_tags
# This filename is the name we are going to use when loading the tags in the template file

from django import template

register = template.Library()

@register.filter
def to_upper(value):
    return str(value).upper()

def to_lower(value):
    return str(value).lower()

# Give a custom name instead of using function name
@register.filter(name="to_camel_case")
def capitalize_first_letter(value):
    str_value = str(value)
    str_value_list = list(str_value)
    str_value_list[0] = str_value_list[0].upper()
    return "".join(str_value_list)

# Registering filters without using annotations
register.filter("to_lower", to_lower)