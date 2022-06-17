from django.forms import model_to_dict
from django.http import JsonResponse
from yaml import serialize

from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    ''' DRF API view
    '''
    instance = Product.objects.all().order_by('?').first()
    data ={}
    if instance:
    #    data= model_to_dict(instance, fields=['id','title','content', 'price'])
        data = ProductSerializer(instance).data
    return Response (data)

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    ''' DRF API view'''
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        return Response (serializer.data)