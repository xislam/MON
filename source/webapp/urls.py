from django.urls import path

from webapp.views import NPAListView
from . import views

urlpatterns = [
    path('npa/', NPAListView.as_view(), name="NPA"),
]
