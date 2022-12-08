from django.urls import path
from product.views import *

app_name = "product"
urlpatterns = [
    path('',index_view,name="index"),
    path('api_view',view_api,name="view_api"),
    path('api_view/<id>/',detail_api,name="detail_api"),
    path('product_detail/<slug>/',product_detail,name="product_detail"),
    path('product_delete/<id>/',delete_product,name="delete_product"),
    path("wish/",wishlist_view, name="wish"),
    path('user_wishlist/',wishlist_product_view,name="user_wishlist"),
    path('cart/', show_cart, name='showcart'),
    path('pluscart/', plus_cart),
    path('minuscart/', minus_cart),
    path('removecart/', remove_cart),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('checkout/', checkout, name='checkout'),
    path('paymentdone/', payment_done, name='paymentdone'),

    path('orders/',orders,name="invoice"),
    path('notifications/',notifications,name="notifications"),
    path('order_detail/<id>/',order_detail,name="order_detail"),
    path('seller_order/',seller_orders,name="seller_order"),

    
]
