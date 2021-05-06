from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('passport', 'tel_number',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'number_auto', 'gear_box',)
    list_filter = ('car_brand', 'gear_box',)
@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'passport', 'car_number',  'time_and_price',)
    list_filter = ('car_brand', 'car_model', 'time_and_price')

class TimPrAdmin(admin.ModelAdmin):
    list_display = ('time_and_price', 'price')

admin.site.register(Person, UserAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Time_and_Price, TimPrAdmin)
#admin.site.register(Rent)
