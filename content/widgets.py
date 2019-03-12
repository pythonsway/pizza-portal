from django.forms.widgets import Textarea


class WYSIWYGTextarea(Textarea):
    template_name = 'content/widgets/wysiwyg.html'
