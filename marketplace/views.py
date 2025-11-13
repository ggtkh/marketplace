from django.shortcuts import render
from django.http import HttpResponse
from .models import Good, SavedCharacteristics

# Create your views here.


def index(request):
    goods = Good.objects.all()
    return render(request, 'goods.html', {'goods': goods})

def test_page(request):
    goods = Good.objects.all()
    return render(request, 'testpage.html', {'goods': goods})

def goods(request):
    goods = Good.objects.all()
    saved_chars = SavedCharacteristics.objects.get(id=1)
    manufacturers = saved_chars.manufacturers
    ipses = saved_chars.ipses
    cpus = saved_chars.cpus
    rams = saved_chars.rams
    ssds = saved_chars.ssds
    return render(request, 'goods.html', {'goods': goods,
                                          'manufacturers': manufacturers,
                                          'ipses': ipses,
                                          'cpus': cpus,
                                          'rams': rams,
                                          'ssds': ssds,})