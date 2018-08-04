"""erpzinho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products.views import product_request, AboutView
from products.views import api_product_list
from provider.views import ProviderListApiView
from provider.views import ProviderDetailApiView
from products.views import ProductDetailView, ProductListView
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/products/', api_product_list),
    path('api/providers/', ProviderListApiView.as_view()),
    path('api/providers/<int:pk>/', ProviderDetailApiView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('about/', AboutView.as_view()),
    path('request/products/', product_request),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
