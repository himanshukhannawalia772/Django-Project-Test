from django.urls import path
from . import views

urlpatterns=[
    path('add/',views.add_product,name='add-product'),
    path('search/',views.search,name='search'),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_view,name='product-view'),
    path('<slug:category_slug>/',views.category,name='category'),
]