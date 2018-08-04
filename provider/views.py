from rest_framework import generics
from .serializers import ProviderSerializer
from .models import Provider


class ProviderListApiView(generics.ListCreateAPIView):

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetailApiView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
