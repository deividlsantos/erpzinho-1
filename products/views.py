from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
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

    def get_context_data(self, **kwargs):
        context = super

def about(request):
    return render(request, "about.html")