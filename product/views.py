
from django.shortcuts import render,get_object_or_404,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Basket, MainCategory,SubCategory,Product,AdsSettings, User, Invoice, Notification
from product.serializers import ProductSerializer
from django.http import HttpResponse
from django.template.defaulttags import register
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from users.forms import ChangeStatusForm


# Create your views here.


def index_view(request):
    main_categories = MainCategory.objects.all()
    ads = AdsSettings.objects.all()
    sub_categories = SubCategory.objects.all()
    products = Product.objects.all()

    context = {
        "main_categories":main_categories,
        "ads":ads,
        "sub_categories":sub_categories,
        "products":products
    }

    
    return render(request,'homepage/homepage-3.html',context)

def product_detail(request,slug):
    context = {}
    product = get_object_or_404(Product,slug=slug)
    context['product'] = product


    return render(request,"product_detail/product_detail.html",context)

def delete_product(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect(request.META['HTTP_REFERER'])
    



@api_view(['GET'])
def view_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail_api(request,id):
    products = Product.objects.filter(id=id)
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)


@register.filter
def exclude_product(self,product):
    result = self.exclude(id=product.id)
    return result



def wishlist_view(request):
    if not request.user.is_authenticated:
        return JsonResponse('In order to add products to wishlist, authenticate first', status=401, safe=False)

    data = {}
    id = request.POST.get("id")
    product = get_object_or_404(Product, id=int(id))

    if request.user in product.wishlist.all():
        data['success'] = False
        product.wishlist.remove(request.user)
    else:
        product.wishlist.add(request.user)
        data['success'] = True

    product.save()
    return JsonResponse(data)

@login_required(login_url="/login/")
def wishlist_product_view(request):
    context = {}

    products = Product.objects.filter(wishlist__in=[request.user])

    context["products"] = products
    return render(request, "user/user_buyer/wishlist/whishlist.html", context)


# def add_basket_view(request):
#     data = {}

#     id = request.POST.get("id")
#     product = get_object_or_404(Product, id=int(id))

#     if not Basket.objects.filter(product=product, user=request.user).exists():
#         Basket.objects.create(
#             product=product, user=request.user
#         )

#     data['basket_count'] = Basket.objects.filter(user=request.user).count()
#     return JsonResponse(data)


@login_required(login_url="/login/")
def add_to_cart(request):
	user = request.user
	item_already_in_cart1 = False
	product = request.GET.get('prod_id')
	item_already_in_cart1 = Basket.objects.filter(Q(product=product) & Q(user=request.user)).exists()
	if item_already_in_cart1 == False:
		product_title = Product.objects.get(id=product)
		Basket(user=user, product=product_title).save()
		messages.success(request, 'Product Added to Cart Successfully !!' )
		return redirect('/')
	else:
		return redirect('/')

@login_required(login_url="/login/")
def checkout(request):
	user = request.user
	add = user
	cart_items = Basket.objects.filter(user=request.user)
	return render(request, 'user/checkout.html', {'add':add, 'cart_items':cart_items})


@login_required(login_url="/login/")
def payment_done(request):
	custid = request.GET.get('custid')
	print("Customer ID", custid)
	user = request.user
	cartid = Basket.objects.filter(user = user)
	customer = User.objects.get(id=user.id)
	print(customer)
	for cid in cartid:
		Invoice(user=cid.product.seller, customer=customer, product=cid.product, quantity=cid.quantity).save()
		Notification(title="You ordered item", user=customer,content="You succesfully ordered item").save()
		print("Order Saved")
		cid.delete()
		print("Cart Item Deleted")
	return redirect("/")


@login_required(login_url="/login/")
def orders(request):
	context = {}
	orders = Invoice.objects.filter(customer=request.user)
	context['orders'] = orders

	return render(request,"user/user_buyer/invoice/invoices.html",context)


@login_required(login_url="/login/")
def seller_orders(request):
	context = {}
	
	form = ChangeStatusForm()
	if request.method == "POST":
		id=request.POST.get('smth')
		
		order = get_object_or_404(Invoice,id=id)
		form = ChangeStatusForm(request.POST,instance=order)
		if form.is_valid():
			
			form.save()
			return HttpResponseRedirect('/seller_order')
		else:
			form = ChangeStatusForm(instance=order)

	context['form'] = form
	orders = Invoice.objects.filter(user=request.user).order_by('-ordered_date')


	context['orders'] = orders
	

	return render(request,"user/user_seller/seller_orders.html",context)

@login_required(login_url="/login/")
def order_detail(request,id):
	context = {}
	order = get_object_or_404(Invoice,id=id)
	context['order'] = order

	return render(request,"user/user_buyer/invoice/invoice-detail.html",context)

@login_required(login_url="/login/")
def notifications(request):
	context = {}
	notifications = Notification.objects.filter(user=request.user)
	context['notifications'] = notifications

	return render(request,"user/user_buyer/notifications/notifications.html",context)


@login_required(login_url="/login/")
def show_cart(request):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Basket.objects.filter(user=request.user))
		user = request.user
		cart = Basket.objects.filter(user=user)
		amount = 0.0
		shipping_amount = 70.0
		totalamount=0.0
		cart_product = [p for p in Basket.objects.all() if p.user == request.user]
		
		if cart_product:
			for p in cart_product:
				p.product.tempamount = (p.quantity * p.product.discount)
				p.product.save()
				amount += p.product.tempamount
				totalamount = amount+shipping_amount
			return render(request, 'user/user_buyer/basket.html', {'carts':cart, 'amount':amount, 'totalamount':totalamount, 'totalitem':totalitem})
		else:
			return render(request, 'user/user_buyer/basket.html', {'totalitem':totalitem})
	else:
		return render(request, 'user/user_buyer/basket.html', {'totalitem':totalitem})


def plus_cart(request):
	if request.method == 'GET':
		prod_id = request.GET['prod_id']
		c = Basket.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.quantity+=1
		
		c.save()
		c.product.tempamount = ((c.quantity * c.product.discount))
		c.save()
		amount = 0.0
		shipping_amount= 70.0
		cart_product = [p for p in Basket.objects.all() if p.user == request.user]
		for p in cart_product:
			tempamount = (p.quantity * p.product.discount)
			
			
			# print("Quantity", p.quantity)
			# print("Selling Price", p.product.discounted_price)
			# print("Before", amount)
			amount += tempamount
			# print("After", amount)
		# print("Total", amount)
			p.product.save()
		data = {
			'tempamount':c.product.tempamount,
			'quantity':c.quantity,
			'amount':amount,
			'totalamount':amount+shipping_amount
		}
		return JsonResponse(data)
	else:
		return HttpResponse("")

def minus_cart(request):
	if request.method == 'GET':
		prod_id = request.GET['prod_id']
		c = Basket.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.quantity-=1
		
		

		c.save()
		c.product.tempamount = ((c.quantity * c.product.discount))
		c.save()
		amount = 0.0
		shipping_amount= 70.0
		cart_product = [p for p in Basket.objects.all() if p.user == request.user]
		for p in cart_product:
			tempamount = (p.quantity * p.product.discount)
			
			# print("Quantity", p.quantity)
			# print("Selling Price", p.product.discounted_price)
			# print("Before", amount)
			amount += tempamount
			# print("After", amount)
		
		# print("Total", amount)
		data = {
			'tempamount':c.product.tempamount,
			'quantity':c.quantity,
			'amount':amount,
			'totalamount':amount+shipping_amount
		}
		return JsonResponse(data)
	else:
		return HttpResponse("")


def remove_cart(request):
	if request.method == 'GET':
		prod_id = request.GET['prod_id']
		c = Basket.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.delete()
		amount = 0.0
		shipping_amount= 70.0
		cart_product = [p for p in Basket.objects.all() if p.user == request.user]
		for p in cart_product:
			tempamount = (p.quantity * p.product.discount)
			# print("Quantity", p.quantity)
			# print("Selling Price", p.product.discounted_price)
			# print("Before", amount)
			amount += tempamount
			# print("After", amount)
		# print("Total", amount)
		data = {
			'amount':amount,
			'totalamount':amount+shipping_amount
		}
		return JsonResponse(data)
	else:
		return HttpResponse("")



