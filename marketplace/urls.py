from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('test_page/', views.test_page, name='test_page'),
    path('goods/', views.goods, name='goods'),
    path('goods/<int:good_id>/', views.single_good, name='single_good')
]