from django.db import models

class Products(models.Model):
    # id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    details=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    ratings=models.FloatField()
    image=models.ImageField()
    
    def __str__(self) -> str:
        return self.name
    

class Sales(models.Model):
    name=models.CharField(max_length=255)
    offer_price=models.IntegerField()
    payment_method=models.CharField(max_length=255)
    transaction_Id=models.CharField(max_length=255)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


