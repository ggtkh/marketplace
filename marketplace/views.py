from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Good, SavedCharacteristics
from .search_by_trigrams import search_by_name
from .forms import GoodForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def index(request):
    # goods = Good.objects.all()
    return render(request, 'main_page.html', {})

def about_us(request):
    return render(request, 'about_us.html', {})

def goods(request):
    goods = Good.objects.all()
    saved_chars = SavedCharacteristics.objects.get(id=1)
    manufacturers = saved_chars.manufacturers

    matrixes = saved_chars.matrixes
    cpus = saved_chars.cpus
    gpus = saved_chars.gpus
    rams = saved_chars.rams
    ssds = saved_chars.ssds
    min_price, max_price = saved_chars.min_price, saved_chars.max_price
    if request.method == "POST":
        list_m = request.POST.getlist('manufacturer')
        list_r = request.POST.getlist('ram')
        list_mtx = request.POST.getlist('matrix')
        list_s = request.POST.getlist('ssd')
        list_c = request.POST.getlist('cpu')
        list_g = request.POST.getlist('gpu')
        
        selected_price = int(request.POST.get('slider'))
        
        search_text = str(request.POST.get('searching'))

        filtered_goods = []
        
        for good in goods:
            if list_m and good.manufacturer not in list_m:
                continue
            if list_r and good.characteristics['RAM'] not in list_r:
                continue
            if list_mtx and good.characteristics['matrix'] not in list_mtx:
                continue
            if list_s and good.characteristics['SSD'] not in list_s:
                continue
            if list_c and good.characteristics['CPU'] not in list_c:
                continue
            if list_g and good.characteristics['GPU'] not in list_g:
                continue
            if selected_price and not good.price <= selected_price:
                continue

            filtered_goods.append(good)

        if search_text:
            filtered_goods = search_by_name(filtered_goods, search_text, match=1)
            print(filtered_goods)

        print(request.POST.get('searching'))

        goods = filtered_goods

        return render(request, 'goods.html', {'goods': goods,
                                            'manufacturers': manufacturers,

                                            'matrixes': matrixes,
                                            'cpus': cpus,
                                            'gpus': gpus,
                                            'rams': rams,
                                            'ssds': ssds,
                                            'min_price': min_price,
                                            'max_price': max_price,

                                            'selected_m': list_m,
                                            'selected_r': list_r,
                                            'selected_mtx': list_mtx,
                                            'selected_s': list_s,
                                            'selected_c': list_c,
                                            'selected_g': list_g,
                                            'selected_price': selected_price,

                                            'filtered_goods': filtered_goods},)
    else:
        return render(request, 'goods.html', {'goods': goods,
                                            'manufacturers': manufacturers,
                                            'matrixes': matrixes,
                                            'cpus': cpus,
                                            'gpus': gpus,
                                            'rams': rams,
                                            'ssds': ssds,
                                            'min_price': min_price,
                                            'max_price': max_price,})
    

def single_good(request, good_id):
    good = Good.objects.get(id=good_id)
    return render(request, 'single_good.html', {'good': good},)


@staff_member_required
def edit_good(request, good_id):
    good = Good.objects.get(id=good_id)

    if request.method == 'POST':
        form = GoodForm(request.POST, instance=good)
        if form.is_valid():
            form.save()
            redirect('single_good', good_id=good_id)
    else:
        form = GoodForm(instance=good)

    return render(request, 'edit_single_good.html', {'form': form,
                                                     'good_id': good_id,})