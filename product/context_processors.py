from django.contrib.auth.decorators import login_required
from product.models import Basket


# @login_required(login_url="/login/")
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
			return {'carts':cart, 'amount':amount, 'totalamount':totalamount, 'totalitem':totalitem}
		else:
			return {'totalitem':totalitem}
	else:
		return {'totalitem':totalitem}
