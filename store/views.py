from django.shortcuts import render
from .models import Product
from category.models import Category


# Create your views here.
def store(request):
    categories = Category.objects.all()
    selected_category_id=request.POST.get('category_id')
    products = None

    if selected_category_id:
        try:
            selected_category = Category.objects.get(id=selected_category_id)
            products =Product.objects.filter(category=selected_category,is_available=True)
        except Category.DoesNotExist:
            products = Product.objects.filter(is_available=True)
        product_count = products.count()

    else:
        products =Product.objects.filter(is_available=True)
        product_count = products.count()
    context = {
        'products':products,
        'categories' :categories,
        'product_count' : product_count,
    }
    return render(request,'store/store.html',context)


def product_detail(request,category_id,product_id,selected_image=None):
    categories=Category.objects.all()
    try:
        selected_category = Category.objects.get(id=category_id)
        single_product=Product.objects.get(category=selected_category, id=product_id, is_available=True)
        product_images = single_product.images.all()
    except Exception as e:
        raise e
    
    context = {
        'single_product' : single_product,
        'product_images' : product_images,
        
    }
    return render(request,'store/product_detail.html',context)
 