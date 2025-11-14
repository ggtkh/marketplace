from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('goods/', views.goods, name='goods'),
    path('goods/<int:good_id>/', views.single_good, name='single_good'),
    path('about_us/', views.about_us, name='about_us'),
]