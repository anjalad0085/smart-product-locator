from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_product, name='search_product'),
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/products/', views.product_list, name='product_list'),
    path('admin-panel/product/<int:id>/', views.product_form, name='edit_product'),
    path('admin-panel/product/', views.product_form, name='product_form'),
    path('admin-panel/delete/<int:id>/', views.delete_product, name='delete_product'),
    path('admin-login/', views.admin_login, name='admin_login'),
path('admin-logout/', views.admin_logout, name='admin_logout'),
]