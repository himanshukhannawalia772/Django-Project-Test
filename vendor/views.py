from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render,redirect
from .models import Vendor
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def become_vendor(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST or None)
        if form.is_valid():
            user=form.save()
            vendor=Vendor.objects.create(name=user.username,created_by=user)
            login(request,user)
            messages.SUCCESS(f'user has been created')       
            return redirect('core:frontpage')

    else:
        user=UserCreationForm()
        context={'form':user}
        return render(request,template_name='vendor/become_vendor.html',context=context)

login_required
def vendor_admin(request):
    vendor=request.user.vendor
    products=vendor.products.all()
    return render(request,template_name='vendor/vendor_admin.html',context={'vendor':vendor,'products':products})

