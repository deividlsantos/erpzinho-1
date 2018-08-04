from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer



class ProductListView(ListView):

    model = Product
    queryset = Product.objects.filter(pk__gte=1)
    template_name = "product_list.html"
    context_object_name = 'products'
    paginate_by = 3


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


def api_product_list(request):

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)