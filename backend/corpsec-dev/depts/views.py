from django.shortcuts import render

from django.views import generic
from .models import Department


class CompanyListView(generic.ListView):
    model = Department
    
