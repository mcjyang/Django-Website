from django.conf.urls import url, include
from django.contrib import admin
from . import views
from . import api


urlpatterns = [
    url(r'^home/', views.home, name = 'home'),
    # url(r'^api/', include(router.urls))
    url(r'^api/product/$', api.product_list),
    url(r'^api/product/(?P<pk>[0-9]+)/$', api.product_detail),
]
