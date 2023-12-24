from rest_framework import serializers
from .models import *
from product.serialazers import *

class cartserializer(serializers.ModelSerializer):
    class Meta:
        model = cart

        fields = '__all__'

class cartItemsSerializer(serializers.ModelSerializer):
    cart = cartserializer()
    product = ProductSerializer()

    class Meta:
        models = cartItems
        fields = '__all__'

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        models = orders
        fields = '__all__'