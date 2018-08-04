from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import FormParser
from .serializers import ProviderSerializer
from .models import Provider


@csrf_exempt
def api_providers(request):
    if request.method == 'GET':
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = FormParser().parse(request)
        serializer = ProviderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result' : 'ok'}, status=201)
        return JsonResponse(serializer.errors, status=400)