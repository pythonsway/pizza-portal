from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from .widgets import WYSIWYGTextarea

# WYSIWYG for Flatpages
class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': WYSIWYGTextarea}
    }

    class Media:
        css = {
            'all': ('content/trumbo/ui/trumbowyg.min.css',)
        }
        js = ('https://code.jquery.com/jquery-3.3.1.min.js',)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)
