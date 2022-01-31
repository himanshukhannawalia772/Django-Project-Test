from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.shortcuts import redirect
from .models import Category,Product
import random
from django.db.models import Q
from django.contrib import messages
from cart.cart import Cart
from cart.forms import AddToCartForm

login_required
def add_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            product=form.save(commit=False)
            product.vendor=request.user.vendor
            product.slug=slugify(product.title)
            product.save()
            return redirect('vendor-admin')
    else:
        form=ProductForm()
    return render(request,template_name='product/add-product.html',context={'form':form})

def product_view(request,category_slug,product_slug):
    cart=Cart(request)
    product=get_object_or_404(Product,category__slug=category_slug,slug=product_slug)
    
    if request.method=='POST':
        form=AddToCartForm(request.POST)
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            if form.is_valid():
                quantity=form.cleaned_data.get('quantity')
                
                cart.add(product_id=product.id,quantity=quantity,update_quantity=False)
                messages.success(request,'The product was added to cart.')
                
                return redirect('product-view',category_slug=category_slug,product_slug=product_slug)
        else:
            return redirect('login')
    else:
        form=AddToCartForm()

    similar_products=list(product.category.products.exclude(id=product.id))

    if len(similar_products)>=4:
        similar_products=random.sample(similar_products,4)
    return render(request,template_name='product/product.html',context={'form':form,'similar_products':similar_products,'product':product})


def category(request,category_slug):
    category=get_object_or_404(Category,slug=category_slug)
    return render(request,template_name='product/category.html',context={'category':category})


def search(request):
    query=request.GET.get('query','')
    products=Product.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
    return render(request,template_name='product/search.html',context={'products':products,'query':query})