from django.shortcuts import render, redirect
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
    if request.method == "POST":
        list_m = request.POST.getlist('manufacturer')
        list_r = request.POST.getlist('ram')
        list_i = request.POST.getlist('ips')
        list_s = request.POST.getlist('ssd')
        list_c = request.POST.getlist('cpu')
        selected_price = int(request.POST.get('slider'))

        filtered_goods = []
        
        for good in goods:
            if list_m and good.manufacturer not in list_m:
                continue
            if list_r and good.characteristics['RAM'] not in list_r:
                continue
            if list_i and good.characteristics['IPS'] not in list_i:
                continue
            if list_s and good.characteristics['SSD'] not in list_s:
                continue
            if list_c and good.characteristics['CPU'] not in list_c:
                continue
            if selected_price and not good.price <= selected_price:
                continue

            filtered_goods.append(good)

        goods = filtered_goods

        return render(request, 'goods.html', {'goods': goods,
                                            'manufacturers': manufacturers,

                                            'ipses': ipses,
                                            'cpus': cpus,
                                            'rams': rams,
                                            'ssds': ssds,

                                            'selected_m': list_m,
                                            'selected_r': list_r,
                                            'selected_i': list_i,
                                            'selected_s': list_s,
                                            'selected_c': list_c,
                                            'selected_price': selected_price,

                                            'filtered_goods': filtered_goods},)
    else:
        return render(request, 'goods.html', {'goods': goods,
                                            'manufacturers': manufacturers,
                                            'ipses': ipses,
                                            'cpus': cpus,
                                            'rams': rams,
                                            'ssds': ssds,})
    

def single_good(request, good_id):
    good = Good.objects.get(id=good_id)
    return render(request, 'single_good.html', {'good': good},)