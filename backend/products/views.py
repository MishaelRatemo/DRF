from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# can be use as a post method making work easy
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def perform_create(self, serializer):
    #     # serializer.save(user=self.request.user)
    #     title = serializer.validated_data.get('title')
    #     content = serializer.validated_data.get('data')
        
    #     if content is None:
    #         content =title
    #     serializer.save(content=content)
        # you can send a Django signal here

class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
