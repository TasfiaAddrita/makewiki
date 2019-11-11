from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from .models import Page
from .forms import PageModelForm

# Create your views here.

class PageCreateView(CreateView):
    template_name = 'page_update.html'
    form_class = PageModelForm
    queryset = Page.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class PageListView(ListView):
    """
    CHALLENGES:
      1. On GET, display a homepage that shows all Pages in your wiki.
      2. Replace this CHALLENGE text with a descriptive docstring for PageList.
      3. Replace pass below with the code to render a template named `list.html`.
    """
    # model = Page
    template_name = 'page_list.html'
    queryset = Page.objects.all()

    # def get(self, request):
    #     """ Returns a list of wiki pages. """
    #     context = {
    #       'wikis': Page.objects.all()
    #     }
    #     return render(request, 'list.html', context=context)

class PageDetailView(DetailView):
    """
    CHALLENGES:
      1. On GET, render a template named `page.html`.
      2. Replace this docstring with a description of what this accomplishes.

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
    """
    model = Page
    template_name = 'page_detail.html'
    # queryset = Page.objects.all()

    # def get(self, request, slug):
    #     """ Returns a specific of wiki page by slug. """
    #     context = {
    #       'wiki': Page.objects.get(slug=slug),
    #     }
    #     return render(request, 'page.html', context=context)

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Page, slug=slug)

class PageUpdateView(UpdateView):
    template_name = 'page_update.html'
    form_class = PageModelForm

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Page, slug=slug)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)