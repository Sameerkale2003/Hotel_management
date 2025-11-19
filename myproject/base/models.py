from django.db import models


class Room(models.Model):
    room_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=30)
    room_desc = models.CharField(max_length=30)
    price_per_night = models.CharField(max_length=20)
    is_available = models.CharField(max_length=10)
    
class Guest(models.Model):
    room_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=30)
    room_desc = models.CharField(max_length=30)
    price_per_night = models.CharField(max_length=20)
    is_available = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    
class History(models.Model):
    room_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=30)
    room_desc = models.CharField(max_length=30)
    price_per_night = models.CharField(max_length=20)
    is_available = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    
    
    
    