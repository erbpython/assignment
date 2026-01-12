from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=20, primary_key=True)
    customer_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    
    def __str__(self):
        return self.customer_name


class Product(models.Model):
    product_id = models.CharField(max_length=20, primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    unit_of_measure = models.CharField(max_length=10)
    standard_cost = models.FloatField()
    list_price = models.FloatField()
    currency = models.CharField(max_length=10)
    origin_country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.product_name


class Trade(models.Model):
    trade_id = models.CharField(max_length=20, primary_key=True)
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="buyer_trades")
    seller = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="seller_trades")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    trade_value = models.FloatField()
    trade_status = models.CharField(max_length=20)
    currency = models.CharField(max_length=10)
    


    def __str__(self):
        return self.trade_id
