from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django import *
from .serialazers import *
# Create your views here.

class cartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self , requset):
        user = requset .user
        cart = cart.objects.filter(user = user , ordered = False).first()
        querset = cart.objects.filter(cart = cart)
        serializer = cartItemsSerializer(querset , many=True)
        return Response(serializer.data)
    
    def POST(self,request):
        data = request.data
        user = request.user
        cart,_ = cart.objects.get_or_create(user = user,ordered=False)

        product = product.objects.get(id = data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        cart_items = cart(cart=cart,user=user,product=product,price=price,quantity=quantity)
        cart_items.save()

        total_price =0
        cart_items=cart.objects.filter(user = user,cart=cart.id)
        for items in cart_items:
            total_price +=items.price
        cart.total_price = total_price
        cart.save()

        return Response({'success':'Items Added to your cart'})


    def put (self,request):
        data= request.data
        cart_items = cart_items.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_items.quantity += quantity
        cart_items.save()
        return Response({'success': 'Items Updated'})   
        

    def delete(self , request):
        user = request .user
        data = request.data
        cart_item = cartItems.objects.get(id=data.get('id'))
        cart_item.delete()
        cart = cart.objects.filter(user = user , ordered = False).first()
        querset = cart.objects.filter(cart = cart)
        serializer = cartItemsSerializer(querset , many=True)
        return Response(serializer.data)
    
class orderdAPI(APIView):
    def get(self , request):
        queryset = orders.objects.filter(user = request.user)
        serializer = orderSerializer(queryset ,many=True)
        return Response(serializer)
    