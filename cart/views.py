import stripe
from django.shortcuts import render,redirect
from .cart import Cart
from django.contrib import messages
from django.conf import settings
from .forms import CheckOutForm
from order.utilities import checkout

def cart_detail(request):
    cart = Cart(request)
    
    if request.method=='POST':
        form=CheckOutForm(request.POST or None)
        if form.is_valid():
            stripe.api_key=settings.STRIPE_SECRET_KEY

            stripe_token=form.cleaned_data['stripe_token']
            charge=stripe.Charge.create(
                amount=int(cart.get_total_costs() * 100),
                currency='INR',
                description='Charge from InteriorShop',
                source=stripe_token
            )
        
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            address=form.cleaned_data['address']
            zipcode=form.cleaned_data['zipcode']
            place=form.cleaned_data['place']

            order=checkout(request,first_name,last_name,email,address,zipcode,place,phone,cart.get_total_costs())
            cart.clear()
            return redirect('success')
    else:
        form=CheckOutForm()

    remove_from_cart = request.GET.get('remove_from_cart', '')
    quantity=request.GET.get('quantity',0)
    change_quantity=request.GET.get('change_quantity','')

    if remove_from_cart:
        cart.remove(remove_from_cart)
        return redirect('cart')

    if change_quantity:
        cart.add(change_quantity,quantity,True)
        return redirect('cart')

    return render(request, template_name='cart/cart.html',context={'form':form,'stripe_pub_key':settings.STRIPE_PUB_KEY})


def success(request):
    return render(request,'cart/success.html')