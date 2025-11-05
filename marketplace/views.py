from django.shortcuts import render
from django.http import HttpResponse
from .models import Good

# Create your views here.

def index(request):
    goods = Good.objects.all()
    return render(request, 'testpage.html', {'goods': goods})