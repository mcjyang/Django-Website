from django.conf.urls import url, include
from django.contrib import admin
from . import views
from . import api


urlpatterns = [
    
    url(r'^admin/$', views.admin, name = 'product_admin'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^api/$', api.product_list, name = 'product_list'),
    url(r'^api/(?P<pk>[0-9]+)/$', api.product_detail, name = 'product_detail'),
    
]
