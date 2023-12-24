from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
# Create your models here.


class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField (default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.username)+" "+ str(self.total_price)


class cartItems(models.Model):
    cart = models.ForeignKey(cart,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.SlugField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username)+" "+str(self.product.product_name)

@receiver(post_save, sender=cartItems)
def correct_price(sender, **kwargs):
    
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * int(price_of_product.price)
    # total_cart_items = cartItems.objects.filter(user = cart_items.user)
    # cart = cart.objects.get(id = cart_items.cart.id)
    # cart.total_price = cart_items.price
    # cart.save()

class orders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cart = models.ForeignKey(cart,on_delete=models.CASCADE)
    amount = models.FloatField(default=False)
    is_paid = models.BooleanField(default=100,blank=True)
    payment_signature = models.CharField(max_length=100,blank=True)

class orderedItems(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.ForeignKey(orders,on_delete=models.CASCADE)