from django.urls import path, re_path, include
from . import views
from django.contrib import admin
from .views import SearchResultsView

urlpatterns = [
    re_path(r'^export-csv/$', views.export, name='export'),
    path('', views.database_home, name='database_home'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('add_complaints', views.add_complaints, name='add_complaints'),
    path('search/', SearchResultsView.as_view(), name='search')
]