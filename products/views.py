from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
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


class AboutView(TemplateView):

    template_name = "about.html"


class ProductDetailView(DetailView):

    slug_field = 'id'
    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'

