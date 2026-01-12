import pandas as pd
from django.core.management.base import BaseCommand
from trading.models import Customer, Product, Trade

class Command(BaseCommand):
    help = "Import cleaned CSV files into database"

    def handle(self, *args, **kwargs):
        customers = pd.read_csv("customers_clean.csv")
        products = pd.read_csv("products_clean.csv")
        trades = pd.read_csv("trades_clean.csv")

        for _, row in customers.iterrows():
            Customer.objects.update_or_create(
                customer_id=row["CustomerID"],
                defaults={
                    "customer_name": row["CustomerName"],
                    "country": row["Country"],
                    "city": row["City"],
                    "email": row["Email"],
                    "phone": row["Phone"],
                     }
            )

        for _, row in products.iterrows():
            Product.objects.update_or_create(
                product_id=row["ProductID"],
                defaults={
                    "product_name": row["ProductName"],
                    "category": row["Category"],
                    "unit_of_measure": row["UnitOfMeasure"],
                    "standard_cost": row["StandardCost"],
                    "list_price": row["ListPrice"],
                    "currency": row["Currency"],
                    "origin_country": row["OriginCountry"],
                    
                }
            )

        for _, row in trades.iterrows():
            Trade.objects.update_or_create(
                trade_id=row["TradeID"],
                defaults={
                    "buyer": Customer.objects.get(customer_id=row["BuyerID"]),
                    "seller": Customer.objects.get(customer_id=row["SellerID"]),
                    "product": Product.objects.get(product_id=row["ProductID"]),
                    "quantity": row["Quantity"],
                    "unit_price": row["UnitPrice"],
                    "trade_value": row["TradeValue"],
                    "trade_status": row["TradeStatus"],
                    "currency": row["Currency"],   
                }
            )

        self.stdout.write(self.style.SUCCESS("✅ CSV data imported successfully"))
