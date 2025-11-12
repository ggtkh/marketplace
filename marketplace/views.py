from django.shortcuts import render
from django.http import HttpResponse
from .models import Good

# Create your views here.


def index(request):
    goods = Good.objects.all()
    return render(request, 'goods.html', {'goods': goods})

def test_page(request):
    goods = Good.objects.all()
    return render(request, 'testpage.html', {'goods': goods})

def goods(request):
    goods = Good.objects.all()
    manufacturers = Good.manufacturers_list
    ipses = Good.ipses_list
    return render(request, 'goods.html', {'goods': goods,
                                          'manufacturers': manufacturers,
                                          'ipses': ipses,})