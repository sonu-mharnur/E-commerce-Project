from django.shortcuts import render
from .serialazers import *

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({'sucess':"Hurray you are authenticated"})


class Productview(APIView):

    def get(self,request):
        Category = self.request.query_params.get('category')
        if Category:
            queryset = Product.objects.filter(category__category_name = Category)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many = True)
        return Response({'count':len(serializer.data),'data':serializer.data})
       
