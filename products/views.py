from django.shortcuts import render
from .models import Product
from django.db.models import Q

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