from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'passport', 'tel_number', )


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'number_auto', 'gear_box', 'parking', 'auto_service')
    list_filter = ('car_brand', 'gear_box', 'parking', 'auto_service',)


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'passport', 'car_number', 'time_and_price',)
    list_filter = ('car_brand', 'car_model', 'time_and_price', )


class TimPrAdmin(admin.ModelAdmin):
    list_display = ('time_and_price',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('commented_car', 'comment_date_published', 'text_comment')
    list_filter = ('comment_date_published',)


class ParkingAdmin(admin.ModelAdmin):
    list_display = ('parking_name', 'city')
    list_filter = ('parking_name', 'city')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('auto', 'served_or_not_served', 'surname_of_the_mechanic',)
    list_filter = ('auto', 'served_or_not_served',)


class MechanicAdmin(admin.ModelAdmin):
    list_display = ('surname', 'experience', 'tel_number',)
    list_filter = ('experience',)


admin.site.register(Person, UserAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Time_and_Price, TimPrAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Parking, ParkingAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Mechanic, MechanicAdmin)

# admin.site.register(Rent)
