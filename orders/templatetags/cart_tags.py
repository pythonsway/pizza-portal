from django import template


register = template.Library()

#  get class model name
@register.filter
def get_class(self):
    return self.__class__.__name__