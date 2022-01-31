from django import forms

class AddToCartForm(forms.Form):
    quantity=forms.IntegerField()
    

class CheckOutForm(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.CharField(max_length=100)
    address=forms.CharField(max_length=100)
    zipcode=forms.CharField(max_length=100)
    place=forms.CharField(max_length=100)
    stripe_token=forms.CharField(max_length=255)