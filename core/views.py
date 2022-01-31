from django.shortcuts import render
from product.models import Product

def frontpage(request):
    newest_products=Product.objects.all()[0:8]
    return render(request,template_name='core/frontpage.html',context={'newest_products':newest_products})

def contact(request):
    return render(request,template_name='core/contact.html')