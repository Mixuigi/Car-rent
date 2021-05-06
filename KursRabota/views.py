from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import *
import collections
from .models import *
from django.contrib.auth.decorators import login_required
from datetime import timedelta, datetime


def register(request):
    if request.method == "POST":
        u_form = UserForm(request.POST)
        p_form = PersonForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            messages.success(request, f'Registration complete! You may log in!')
            return redirect('authentication')
    else:
        u_form = UserForm(request.POST)
        p_form = PersonForm(request.POST)
    return render(request, 'Register.html', {'u_form': u_form, 'p_form': p_form})


def Authentication(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def Home(request):
    cars = Car.objects.all()
    rents = Rent.objects.all()
    persons = Person.objects.all()
    not_rented_cars = get_not_rented_cars()
    user = Person.objects.get(user=request.user)
    rent = Rent.objects.filter(passport=user.passport).first()

    if rent:
        is_person_has_rent = True
        car = Car.objects.get(number_auto=rent.car_number)

    else:
        is_person_has_rent = False
        car = False

    data = {'cars': cars,
            'persons': persons,
            'rents': rents,
            'not_rented_cars': not_rented_cars,
            'is_person_has_rent': is_person_has_rent,
            'car': car,
            'rent': rent,

            }
    return render(request, 'home.html', data)


def UserCabinet(request, car):
    user = Person.objects.get(user=request.user)
    car = get_object_or_404(Car, number_auto=car)
    if request.method == "POST":
        try:
            create_rent(car, user, request.POST)
        except IntegrityError:
            return HttpResponseRedirect('/')
    data = {
        'car': car,
        'form_rent': RentForm(),
        'passport': user.passport,
        'rents': Rent.objects.all(),  # удалить потом
        #'timeandprice': time_and_price,
    }
    return render(request, 'Kabinet.html', data)


def create_rent(car, user, data):
    rent = RentForm(data)
    if not rent.is_valid():
        return HttpResponse('ошибка валидации')

    hours_from_form = int(str(rent.cleaned_data['time_and_price']).split(' = ')[0][0:-1])

    rent = rent.save(commit=False)
    rent.start_time = datetime.now()
    rent.stop_time = datetime.now() + timedelta(hours=hours_from_form)
    rent.car_model = car.car_model
    rent.car_brand = car.car_brand
    rent.car_number = car.number_auto
    rent.passport = user.passport
    rent.save()


def get_not_rented_cars():
    try:
        rents = Rent.objects.all()
        rented_car_numbers = [rent.car_number for rent in rents]
        not_rented_cars = Car.objects.exclude(number_auto__in=rented_car_numbers)
        return not_rented_cars
    except:
        return []


