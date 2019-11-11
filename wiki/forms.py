from django import forms
from wiki.models import Page


class PageModelForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Page
        fields = '__all__'
