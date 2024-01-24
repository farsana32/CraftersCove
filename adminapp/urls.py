from django.urls import path
from adminapp import views

urlpatterns = [
     path('',views.index,name='index'),
     path('dashboard/', views.dashboard, name='dashboard'),
     path('admin_logout/', views.admin_logout, name='admin_logout'),
     path('admin_products/', views.admin_products, name='admin_products'),
     path('add_product/', views.add_product, name='add_product'),
     path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
     path('soft_delete_product/<int:product_id>/', views.soft_delete_product, name='soft_delete_product'),
     path('undo_soft_delete_product/<int:product_id>/', views.undo_soft_delete_product, name='undo_soft_delete_product'),
     path('admin_category/', views.admin_category, name='admin_category'),
     path('add_category/', views.add_category, name='add_category'),


]