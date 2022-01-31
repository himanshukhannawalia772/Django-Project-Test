from django.db.models.base import Model
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields=['category','image','price','title','description','image_1','image_2','image_3','image_4']