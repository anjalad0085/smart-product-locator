from django.shortcuts import render
from .models import Product
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from .models import Category, Brand

from functools import wraps
from django.shortcuts import redirect

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('is_admin'):
            return redirect('admin_login')
        return view_func(request, *args, **kwargs)
    return wrapper

def home(request):
    return render(request, 'customer/home.html')


def search_product(request):
    query = request.GET.get('q')

    products = []
    recommendations = []

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(brand__name__icontains=query)
        )

        if products.exists():
            # If any product is out of stock → recommend alternatives
            for product in products:
                if product.stock_quantity == 0:
                    recommendations = Product.objects.filter(
                        name__iexact=product.name
                    ).exclude(id=product.id)

        else:
            # If no product found → recommend same category
            recommendations = Product.objects.filter(
                Q(category__name__icontains=query)
            )

    context = {
        'products': products,
        'recommendations': recommendations,
        'query': query
    }

    return render(request, 'customer/home.html', context)

@admin_required
def admin_dashboard(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')

    return render(request, 'custom_admin/dashboard.html')

@admin_required
def product_list(request):
    query = request.GET.get('q')

    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(brand__name__icontains=query)
        )

    return render(request, 'custom_admin/product_list.html', {
        'products': products
    })

@admin_required
def product_form(request, id=None):
    product = None

    if id:
        product = get_object_or_404(Product, id=id)

    categories = Category.objects.all()
    brands = Brand.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        category_name = request.POST.get('category_name')
        brand_name = request.POST.get('brand_name')
        aisle = request.POST.get('aisle')
        rack = request.POST.get('rack')
        stock = request.POST.get('stock')

        # 🔥 Main logic
        category, _ = Category.objects.get_or_create(name=category_name)
        brand, _ = Brand.objects.get_or_create(name=brand_name)

        if product:
            product.name = name
            product.category = category
            product.brand = brand
            product.aisle = aisle
            product.rack = rack
            product.stock_quantity = stock
            product.save()
        else:
            Product.objects.create(
                name=name,
                category=category,
                brand=brand,
                aisle=aisle,
                rack=rack,
                stock_quantity=stock
            )

        return redirect('product_list')

    return render(request, 'custom_admin/product_form.html', {
        'product': product,
        'categories': categories,
        'brands': brands
    })

@admin_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')

def admin_login(request):
    if request.method == 'POST':
        password = request.POST.get('password')

        if password == "admin123":   # 🔥 simple password
            request.session['is_admin'] = True
            return redirect('admin_dashboard')
        else:
            return render(request, 'custom_admin/login.html', {
                'error': 'Invalid password'
            })

    return render(request, 'custom_admin/login.html')


def admin_logout(request):
    request.session.flush()
    return redirect('home')