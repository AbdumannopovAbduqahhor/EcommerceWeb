from django.template import Library

register = Library()


@register.filter
def to_upper(text):
    print(text.upper)
    return text
