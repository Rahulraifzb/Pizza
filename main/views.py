from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PizzaSerializer

from .models import Pizza
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Lists': '/task-pizza',
        'Detail_View': '/pizza-detail/<str:pk>',
        'create': '/pizza-create',
        'update': '/pizza-update',
        'delete': '/pizza-delete',
    }

    return Response(api_urls)


@api_view(['GET'])
def pizzaList(request):
    pizza = Pizza.objects.all()
    serializers = PizzaSerializer(pizza, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def pizzaDetail(request, pk):
    pizza = get_object_or_404(Pizza, id=pk)
    serializers = PizzaSerializer(pizza, many=False)
    return Response(serializers.data)


@api_view(['POST'])
def pizzaCreate(request):
    serializers = PizzaSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(['POST'])
def pizzaUpdate(request, pk):
    pizza = get_object_or_404(Pizza, id=pk)
    serializers = PizzaSerializer(instance=pizza, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(['DELETE'])
def pizzaDelete(request, pk):
    pizza = get_object_or_404(Pizza, id=pk)
    pizza.delete()
    return HttpResponse("Pizza Deleted Successfully!!")
