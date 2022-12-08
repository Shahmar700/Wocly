from itertools import product
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from users.forms import *
from django.contrib.sites.shortcuts import get_current_site
from product.models import Product,ProductImage


# Create your views here.

def buyer_view(request,id):
    context = {}

    usr = get_object_or_404(User, id=id)
    form_b="Buyer"
    form_s="Seller"

    if request.method == 'POST' and 'btn_buyer' in request.POST:
        form = BuyerDetailForm(request.POST, request.FILES or None, instance=usr)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sizin postunuz uğurla yeniləndi!')
            return HttpResponseRedirect('/')
    else:
        form_b = BuyerDetailForm(instance=usr)






        

    if request.method == 'POST' and 'btn_seller' in request.POST:
        form = SellerDetailForm(request.POST, request.FILES or None, instance=usr)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sizin postunuz uğurla yeniləndi!')
            return HttpResponseRedirect('/')
    else:
        form_s = SellerDetailForm(instance=usr)

    context['form_s'] = form_s
    context['form_b'] = form_b
    

    

    return render(request,"user/user_information/user_information.html",context)


# def buyer_notification(request,id):
#     usr = get_object_or_404(User, id=id)

#     return render(request,"user/user_buyer/notifications/notifications.html")

# def buyer_invoice(request,id):
#     usr = get_object_or_404(User, id=id)

#     return render(request,"user/user_buyer/invoice/invoices.html")

# def buyer_wishlist(request,id):
#     usr = get_object_or_404(User, id=id)

#     return render(request,"user/user_buyer/wishlist/whishlist.html")


def buyer_adress(request,id):
    usr = get_object_or_404(User, id=id)

    return render(request,"user/user_buyer/address/addresses.html")



def seller_dashboard(request,id):
    usr = get_object_or_404(User, id=id)

    return render(request,"user/user_seller/seller.html")



def seller_view(request,id):
    context = {}

    usr = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form = SellerDetailForm(request.POST, request.FILES or None, instance=usr)
        if form.is_valid():
            
            
            form.save()
            messages.success(request, 'Sizin postunuz uğurla yeniləndi!')
            return HttpResponseRedirect('/buyer/')
        else:
            context['form'] = form

    context['form'] = SellerDetailForm(instance=usr)


    return render(request,"user/user_information/user_buyer.html",context)



def seller_product(request,id):
    context = {}

    usr = get_object_or_404(User, id=id)

    if request.method == 'POST':

        form = AddProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.seller = usr
            form.save()
            messages.success(request, 'Sizin postunuz uğurla yeniləndi!')
            return redirect(request.META['HTTP_REFERER'])
        else:
            context['form'] = form

    context['form'] = AddProductForm()

    products = Product.objects.filter(seller=usr)
    context['products'] = products




    return render(request,"user/user_seller/seller_product.html",context)

def add_product(request,id):
    context = {}
    
    usr = get_object_or_404(User, id=id)

    if request.method == 'POST':
        images = request.FILES.getlist("image", None)
        form = AddProductForm(request.POST, request.FILES or None)
        if form.is_valid() and images:
            print("I am in is vaild")
            form = form.save(commit=False)
            form.seller = usr
            form.save()
            messages.success(request, 'Sizin postunuz uğurla yeniləndi!')
            for image in images:
                ProductImage.objects.create(
                    product=form, image=image
                )
            # return redirect(request.META['HTTP_REFERER'])
            return redirect("product:index")
        else:
            context['form'] = form

    context['form'] = AddProductForm()

    return render(request,"user/user_seller/add_product.html",context)


# def seller_order(request,id):
#     return render(request,"user/user_seller/seller_orders.html")


def store_view(request,id):
    context = {}
    seller = get_object_or_404(User,id=id)
    store = get_object_or_404(Vendor,seller_id=seller.id)
    
    products = Product.objects.filter(seller=seller)
    context['store'] = store
    context['products'] = products
    return render(request,"user/user_seller/store_detail.html",context)

def store_about(request,id):
    context = {}
    seller = get_object_or_404(User,id=id)
    store = get_object_or_404(Vendor,seller_id=seller.id)
    
    products = Product.objects.filter(seller=seller)
    context['store'] = store
    context['products'] = products
    return render(request,"user/user_seller/store_detail_about.html",context)


def vendor_set(request,id):
    context = {}
    usr = get_object_or_404(User, id=id)
    store = get_object_or_404(Vendor,seller_id=usr.id)
    
    

    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES or None ,instance=store)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sizin postunuz uğurla yeniləndi!')
            return HttpResponseRedirect('/')
    else:
        form = VendorForm(instance=store)

    context['form'] = form

    return render(request,"user/user_seller/vendor_settings.html",context)


def seller_payment(request):
    return render(request,"user/user_seller/seller_payment.html")


# def withdraw(requets,id):
#     return render(request,"user/user_seller/seller_withdraw.html")

