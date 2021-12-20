from django.urls import reverse

from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from polls import forms


class CkEditorFormView(generic.FormView):
    form_class = forms.CkEditorForm
    template_name = "index.html"

    def get_success_url(self):
        return reverse("ckeditor-form")



    def post(self, request):
        data = dict()
        article_create_form = forms.CkEditorForm(request.POST)
        a = request.POST['ckeditor_standard_example']
        f = open('polls/templates/path.html', 'w')
        f.write(a)
        f.close()
        return redirect('ckeditor-form')

ckeditor_form_view = CkEditorFormView.as_view()

class Test(generic.TemplateView):
    template_name = "test.html"
    def get_success_url(self):
        return reverse("test")