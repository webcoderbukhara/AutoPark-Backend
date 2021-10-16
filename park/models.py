from django.db import models

# Create your models here.
class Price(models.Model):
    category = models.CharField(max_length=10)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.category

class Car(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    car_number = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    price = models.ForeignKey(Price,on_delete=models.CASCADE)

    def __str__(self):
        return self.car_number

class CarHistory(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    car_number = models.CharField(max_length=20)
    come_time = models.DateTimeField()
    go_time = models.DateTimeField()
    price = models.ForeignKey(Price,on_delete=models.CASCADE)
    sum = models.FloatField()
    all_time = models.FloatField()

    def __str__(self):
        return self.car_number
    

    def __str__(self):
        return self.car_number