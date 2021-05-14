from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from webapp.models import NPA, News


class NPAListView(ListView):
    template_name = 'NPA.html'
    model = NPA
    ordering = ['-data_cr']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NPAListView, self).get_context_data(**kwargs)
        context["npas"] = NPA.objects.all()
        return context


class IndexView(ListView):
    template_name = '../templates/Ministry of Education and Science/index.html'
    model = News

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["news"] = News.objects.all()
        return context
