from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Good, SavedCharacteristics
from .search_by_trigrams import search_by_name
from .forms import GoodEditForm, GoodCreateForm
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

    screen_diagonals = saved_chars.screen_diagonals
    screen_refresh_rates = saved_chars.screen_refresh_rates
    cpus = saved_chars.cpus
    gpus = saved_chars.gpus
    rams = saved_chars.rams
    storage_capacities = saved_chars.storage_capacities
    min_price, max_price = saved_chars.min_price, saved_chars.max_price
    if request.method == "POST":
        list_m = request.POST.getlist('manufacturer')
        list_r = request.POST.getlist('ram')
        list_sd = request.POST.getlist('screen_diagonals')
        list_srr = request.POST.getlist('screen_refresh_rates')
        list_sc = request.POST.getlist('storage_capacities')
        list_c = request.POST.getlist('cpu')
        list_g = request.POST.getlist('gpu')
        
        selected_price = int(request.POST.get('slider'))
        
        search_text = str(request.POST.get('searching'))

        filtered_goods = []
        
        for good in goods:
            if list_m and good.manufacturer not in list_m:
                continue
            if list_r and good.RAM not in list_r:
                continue
            if list_sd and good.screen_diagonal not in list_sd:
                continue
            if list_srr and good.screen_refresh_rate not in list_srr:
                continue
            if list_sc and good.storage_capacity not in list_sc:
                continue
            if list_c and good.CPU not in list_c:
                continue
            if list_g and good.GPU not in list_g:
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

                                            'diagonals': screen_diagonals,
                                            'refresh_rates': screen_refresh_rates,
                                            'cpus': cpus,
                                            'gpus': gpus,
                                            'rams': rams,
                                            'storage_capacities': storage_capacities,
                                            'min_price': min_price,
                                            'max_price': max_price,

                                            'selected_m': list_m,
                                            'selected_r': list_r,
                                            'selected_diagonals': list_sd,
                                            'selected_refresh_rates': list_srr,
                                            'selected_storages': list_sc,
                                            'selected_c': list_c,
                                            'selected_g': list_g,
                                            'selected_price': selected_price,

                                            'filtered_goods': filtered_goods},)
    else:
        return render(request, 'goods.html', {'goods': goods,
                                            'manufacturers': manufacturers,
                                            'diagonals': screen_diagonals,
                                            'refresh_rates': screen_refresh_rates,
                                            'cpus': cpus,
                                            'gpus': gpus,
                                            'rams': rams,
                                            'storage_capacities': storage_capacities,
                                            'min_price': min_price,
                                            'max_price': max_price,})
    

def single_good(request, good_id):
    good = Good.objects.get(id=good_id)
    return render(request, 'single_good.html', {'good': good},)


@staff_member_required
def edit_good(request, good_id):
    good = Good.objects.get(id=good_id)

    if request.method == 'POST':
        form = GoodEditForm(request.POST, instance=good)
        if form.is_valid():
            form.save()
            redirect('single_good', good_id=good_id)
    else:
        form = GoodEditForm(instance=good)

    return render(request, 'edit_single_good.html', {'form': form,
                                                     'good_id': good_id,})

@staff_member_required
def create_good(request):
    if request.method == 'POST':
        form = GoodCreateForm(request.POST, request.FILES)
        if form.is_valid():
            good = form.save()
            return redirect('single_good', good_id=good.id)
    else:
        form = GoodCreateForm()
    
    return render(request, 'create_good.html', {'form': form,})
