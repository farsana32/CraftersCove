from django.urls import path
from . import views

urlpatterns = [
    path('store/',views.store, name='store'),
    path('product_detail/<int:category_id>/<int:product_id>/',views.product_detail, name='product_detail'),
    
] 