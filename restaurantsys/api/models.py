from django.db import models
from django.utils import timezone
# Create your models here.



class startandentime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class admin(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    
# class OperationalHours(models.Model):
#     open_time = models.TimeField() 
#     close_time = models.TimeField()

class DiningPlace(models.Model):
    admin = models.ForeignKey(admin, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    website = models.URLField()
    starttime = models.TimeField(default=timezone.now)
    endtime = models.TimeField(default=timezone.now)
    operational_hours = models.ManyToManyField(startandentime, through='DiningPlaceOperatingHours')

class Booking(models.Model):
    dining_place = models.ForeignKey(DiningPlace, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Booking for {self.dining_place.name} by {self.user.username}"
    


class DiningPlaceOperatingHours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dining_place = models.ForeignKey(DiningPlace, on_delete=models.CASCADE)
    operational_hours = models.ForeignKey(startandentime, on_delete=models.CASCADE)
    open_time = models.TimeField()
    close_time = models.TimeField()
    

    def __str__(self):
        return self.name
