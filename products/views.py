from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'product_list.html', context)


def product_request(request):
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():

            return HttpResponseRedirect('/products')
    else:
        forms = ProductForm()

    context = {'forms' : forms}
    return render(request, 'product_request.html', context)

