from django.urls import path
from .views import home, all_cars, car_history, create_car, edit

urlpatterns = [
    path('',home, name='home'),
    path('all_cars/',all_cars, name='all_cars'),
    path('cars_history',car_history, name='car_history'),
    path('create_car',create_car, name='create'),
    path('<int:id>/edit/',edit, name='edit'),


    ]