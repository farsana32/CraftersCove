from django.shortcuts import render
from store.models import Product

def home(request):
    products =Product.objects.all().filter(is_available=True)
    context = {
        'products':products,
    }
    for product in products:
        print(product.product_images.url)
    return render(request,'home.html',context)