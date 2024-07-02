from rest_framework import serializers
from .models import User, admin, Booking, startandentime, DiningPlace, DiningPlaceOperatingHours

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'username', 'email', 'password']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields = ['id', 'username', 'email', 'password']

class DiningPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningPlace
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class StartAndEndTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = startandentime
        fields = '__all__'

class DiningPlaceOperatingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningPlaceOperatingHours
        fields = '__all__'
