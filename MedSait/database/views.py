import codecs
import csv

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from .models import Articles, Complaints
from .forms import ArticlesForm, ComplaintsForm
from .admin import ArticlesResource, ComplaintsResource
from django.http import HttpResponse

def database_home(request):
    database = Articles.objects.order_by('name')
    return render(request, 'database/database_home.html', {'database': database})

class SearchResultsView(ListView):
    model = Articles
    template_name = 'database/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Articles.objects.filter(Q(name__icontains=query))
        return object_list

def add_patient(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('database_home')
        else:
            error = 'Ошибка добавления'

    form = ArticlesForm()
    data = {'form': form, 'error': error}
    return render(request, 'database/add_patient.html', data)

def add_complaints(request):
    error = ''
    if request.method == 'POST':
        form = ComplaintsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('database_home')
        else:
            error = 'Ошибка добавления'

    form = ComplaintsForm()
    data = {'form': form, 'error': error}
    return render(request, 'database/add_complaints.html', data)

def export(request):
    complaints_resources = ComplaintsResource()
    dataset = complaints_resources.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Complaints.csv"'
    response.write(u'\ufeff'.encode('utf8'))

    return response

def complaint_list(View):
    complaint = Complaints.objects.count()
    print (complaint)