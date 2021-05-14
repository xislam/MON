from django.urls import path

from webapp.views import NPAListView, IndexView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('npa/', NPAListView.as_view(), name="NPA"),

]
