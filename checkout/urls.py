from django.conf.urls import url
from . import views

urlpatterns = [

    url(
        r'^cart/add/(?P<slug>[\w_-]+)/$', views.create_cartitem,
        name='create_cartitem'
    ),
    url(r'^cart/$', views.cart_item, name='cart_item'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(
        r'^checkout/(?P<pk>\d+)/paypal/$', views.paypal_view,
        name='paypal_view'
    ),
    url(
        r'^checkout/(?P<pk>\d+)/pagseguro/$', views.pagseguro_view,
         name='pagseguro_view'
    ),
    url(r'^order-list/$', views.order_list, name='order_list'),
    url(r'^order-list/(?P<pk>\d+)/$', views.order_detail, name='order_detail'),
]
