from django.urls import path
from users.views import *

app_name="user"

urlpatterns = [
    path('user_info/<id>/',buyer_view,name="user_info"),
    # path('user_notifications/<id>/',buyer_notification,name="user_notf"),
    # path('user_invoice/<id>/',buyer_invoice,name="user_invoice"),
    path('user_adress/<id>/',buyer_adress,name="user_adress"),
    
    path('seller_dashboard/<id>/',seller_dashboard,name ='seller_dashboard'),
    path("seller_product/<id>/",seller_product,name="seller_product"),
    # path("seller_order/<id>/",seller_order,name="seller_order"),
    path("store_seller/<id>/",store_view,name="store_view"),
    path("add_product/<id>/",add_product,name="add_product"),
    path("vendor_settings/<id>/",vendor_set,name="vendor_settings"),
    # path("seller_withdraw/<id>/",withdraw,name="withdraw"),
    path("vendor_about/<id>/",store_about,name="store_about"),
    path('seller_payment/',seller_payment,name="seller_payment")

    ]
