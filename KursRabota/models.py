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


class Parking(models.Model):
    parking_name = models.CharField(max_length=40, blank=True, unique=True)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.parking_name


class Car(models.Model):
    STATUS_CHOICES = (
        ('не была в сервисе', 'Не была в сервисе'),
        ('была в сервисе', 'Была в сервисе'),
    )
    GEAR_BOX_CHOICES = (
        ('механическая', 'Механическая'),
        ('автоматическая', 'Автоматическая'),
        ('электро', 'Электро'),
    )
    BRAND_CHOICES = (
        ('BMW', 'BMW'), ('MERCEDES', 'MERCEDES'), ('AUDI', 'AUDI'), ('MITSUBISHI', 'MITSUBISHI'),
        ('VOLKSWAGEN', 'VOLKSWAGEN'), ('TESLA', 'TESLA'), ('DODGE', 'DODGE'), ('MAZDA', 'MAZDA'),
        ('NISSAN', 'NISSAN'), ('HONDA', 'HONDA'), ('FORD', 'FORD'), ('LADA', 'LADA'), ('KIA', 'KIA'),
        ('RENAULT', 'RENAULT'), ('TOYOTA', 'TOYOTA'), ('SKODA', 'SKODA'),
    )

    car_brand = models.CharField(max_length=10000, choices=BRAND_CHOICES, default='AUDI')
    car_model = models.CharField(max_length=30)
    gear_box = models.CharField(max_length=20, choices=GEAR_BOX_CHOICES, default='механическая')
    number_auto = models.CharField(max_length=30, unique=True)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, null=True, blank=True)
    auto_service = models.CharField(max_length=20, choices=STATUS_CHOICES, default='не была в сервисе')

    def __str__(self):
        return self.number_auto


class Time_and_Price(models.Model):
    time_and_price = models.CharField(max_length=20, blank=True, unique=True)

    def __str__(self):
        return self.time_and_price


class Rent(models.Model):
    passport = models.CharField(max_length=20, blank=True, unique=True)
    car_number = models.CharField(max_length=20, blank=True, unique=True)
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=20)
    car_place = models.CharField(max_length=30)
    time_and_price = models.ForeignKey(Time_and_Price, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    stop_time = models.DateTimeField()


class Comment(models.Model):
    user = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    commented_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    text_comment = models.TextField(max_length=1000)
    comment_date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('comment_date_published',)


class Mechanic(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    tel_number = models.IntegerField()
    experience = models.IntegerField()

    def __str__(self):
        return self.surname


class Service(models.Model):
    STATUS_CHOICES = (
        ('не была в сервисе', 'Не была в сервисе'),
        ('была в сервисе', 'Была в сервисе'),
    )

    auto = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    served_or_not_served = models.CharField(max_length=20, choices=STATUS_CHOICES, default='не была в сервисе')
    surname_of_the_mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE, null=True, blank=True, unique=True)
