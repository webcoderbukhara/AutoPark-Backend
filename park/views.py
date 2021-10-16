from django.shortcuts import render, redirect
from .models import Price, Car, CarHistory
import datetime
from datetime import timedelta, datetime
import math

# Create your views here.
def home(request):
    context={}

    if request.method == 'POST':
        car_number = request.POST.get('car_number')
        car = Car.objects.filter(car_number=car_number)
        context={}
        

        if len(car) != 0:
            car = car[0]
            come_time =car.date
            this_time = datetime.now()
            al_time = str((this_time.timestamp()-come_time.timestamp())/3600)[:5]
            al_time=float(al_time)
            print(al_time)
            if al_time < 1:
                al_time=1
            all_time =  math.ceil((al_time)*10)/10
            print(al_time)
            price = all_time * car.price.price
            context={}
            context['car'] = car
            context['this_time'] = this_time
            context['all_time'] = all_time
            context['price'] = price
            car_in_history = CarHistory(name = car.name, 
                                    phone = car.phone,
                                    car_number = car.car_number,
                                    come_time = come_time,
                                    go_time = this_time,
                                    price = car.price,
                                    sum = price,
                                    all_time = all_time)
            car_in_history.save()
            car.delete()
        else:
            return redirect('create')      
        

    return render(request, 'home.html',context)


def car_history(request):
    context={}
    cars = CarHistory.objects.all()
    if request.method =='POST':
        car_number = request.POST.get('car_number')
        if car_number !='':
            cars = CarHistory.objects.filter(car_number = car_number)

    context['cars'] = cars
    return render(request, 'car_history.html',context)


def all_cars(request):
    context={}
    cars = Car.objects.all()
    context['cars'] = cars

    return render(request, 'all_cars.html',context)


def create_car(request):
    context={}
    prices = Price.objects.all()
    context['price'] = prices

    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        car_number = request.POST.get('car_number')
        price_id = request.POST.get('price')
        price = Price.objects.get(id=price_id)
        car = Car(name=name, phone=phone, car_number=car_number, price=price)
        car.save()

    return render(request, 'create.html',context)



def edit(request,id):
    prices = Price.objects.all()
    car = Car.objects.get(id=id)

    if request.method =="POST":
        car.name = request.POST.get('name')
        car.phone = request.POST.get('phone')
        car.car_number = request.POST.get('car_number')
        car.price_id = request.POST.get('price')
        car.price = Price.objects.get(id=car.price_id)
        # car = Car(name=name, phone=phone, car_number=car_number, price=price)
        car.save()
        return redirect('all_cars')

    return render(request, 'edit.html',{'car':car,'price':prices})

