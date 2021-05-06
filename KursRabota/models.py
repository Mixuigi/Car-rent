from django.db import models
from django.conf import settings
from django.urls import reverse


class Person(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    passport = models.CharField(max_length=9, unique=True)
    tel_number = models.IntegerField()

    def __str__(self):
        return self.passport

    def get_absolute_url(self):
        return reverse('KursRabota:rent_car_passport', args=[self.passport])


class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    car_class = models.CharField(max_length=30)
    gear_box = models.CharField(max_length=30)
    number_auto = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.number_auto

    # def get_absolute_url(self):
    #     return reverse('KursRabota:rent_car_number', args=[self.number_auto])


class Time_and_Price(models.Model):
    time_and_price = models.CharField(max_length=10)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.time_and_price


class Rent(models.Model):
    passport = models.CharField(max_length=20, blank=True,  unique=True)
    car_number = models.CharField(max_length=20, blank=True,  unique=True)
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=20)
    time_and_price = models.ForeignKey(Time_and_Price, on_delete=models.CASCADE)
