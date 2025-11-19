from django.shortcuts import render,redirect
from .models import *


def add_room(request):
    if request.method == "POST":
        room_number_data = request.POST['room_number']
        room_type_data = request.POST['room_type']
        room_desc_data = request.POST['room_desc']
        price_per_night_data = request.POST['price_per_night']
        is_available_data = request.POST['is_available']
        Room.objects.create(
            room_number = room_number_data,
            room_type = room_type_data,
            room_desc = room_desc_data,
            price_per_night = price_per_night_data,
            is_available = is_available_data
            
        )
        return redirect('home')
    
    return render(request,'add_room.html')

def home(request):
    data = Room.objects.all()
    return render(request,'home.html',{'data':data})

def book_now(request,pk):
   data = Room.objects.get(id=pk)
   if request.method == "POST":
       name_data = request.POST['name']
       email_data = request.POST['email']
       phone_number_data = request.POST['phone_number']
       gender_data = request.POST['gender']
       country_data = request.POST['country']
       
       Guest.objects.create(
           name=name_data,
           email=email_data,
           phone_number=phone_number_data,
           gender=gender_data,
           country=country_data,
           room_number=data.room_number,
           room_type=data.room_type,
           room_desc=data.room_desc,
           price_per_night=data.price_per_night,
           is_available=data.is_available
           
       )
       return redirect ('booking')
   return render(request,'book_now.html',{'data':data})


def booking(request):
    data = Guest.objects.all()
    return render(request,'booking.html',{'data':data})
           
def about(request):
    return render(request,'about.html')

def update(request,pk):
    data = Guest.objects.get(id=pk)
    if request.method == "POST":
        name_data = request.POST['name']
        email_data = request.POST['email']
        phone_number_data = request.POST['phone_number']
        gender_data = request.POST['gender']
        country_data = request.POST['country']
        
        data.name = name_data
        data.email = email_data
        data.phone_number = phone_number_data
        data.gender = gender_data
        data.country = country_data
        data.save()
        
        return redirect('booking')
    return render(request,'update.html',{'data':data})


def delete(request,pk):
    a = Guest.objects.get(id=pk)
    print(a)
    History.objects.create(
        room_number=a.room_number,
        room_type=a.room_type,
        room_desc=a.room_desc,
        price_per_night=a.price_per_night,
        is_available=a.is_available,
        name=a.name,
        email=a.email,
        phone_number=a.phone_number,
        gender=a.gender,
        country=a.country
    )
    a.delete()
    return redirect('booking')
    
def history(request):
    data = History.objects.all()
    return render(request,'history.html',{'data':data})

def h_delete(request,pk):
    data = History.objects.get(id=pk)
    data.delete()
    return redirect('history')

def restore(request,pk):
    a = History.objects.get(id=pk)
    Guest.objects.create(
        room_number=a.room_number,
        room_type=a.room_type,
        room_desc=a.room_desc,
        price_per_night=a.price_per_night,
        is_available=a.is_available,
        name=a.name,
        email=a.email,
        phone_number=a.phone_number,
        gender=a.gender,
        country=a.country
        
    )
    a.delete()
    return redirect('booking')
    
    

