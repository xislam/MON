from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from webapp.models import NPA


class NPAListView(ListView):
    template_name = 'NPA.html'
    model = NPA
    ordering = ['-data_cr']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NPAListView, self).get_context_data(**kwargs)
        context["npas"] = NPA.objects.all()
        return context
