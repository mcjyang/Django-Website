from django.conf.urls import url, include
from django.contrib import admin
from . import views
from . import api


urlpatterns = [
	url(r'^accounts/admin/$', views.admin_users, name = 'user_admin'),
	url(r'^accounts/signup/$', views.signup, name = 'signup'),
	url(r'^accounts/login/$', views.login, name = 'login'),
	url(r'^accounts/logout/$', views.logout, name = 'logout'),
	url(r'^accounts/api/(?P<pk>[0-9]+)/$', api.user_detail, name = 'user_detail'),
	url(r'^accounts/api/$', api.user_list, name = 'user_list'),
    
	url(r'^orders/admin/$', views.admin_carts, name = 'order_admin'),
	url(r'^orders/mycart/(?P<pk>[0-9]+)/$', views.mycart, name = 'mycart'),
	url(r'^orders/api/(?P<pk>[0-9]+)/$', api.order_detail, name = 'order_detail'),
	url(r'^orders/api/$', api.order_list, name = 'order_list'),
    
]
