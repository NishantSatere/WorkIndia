from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
from rest_framework import serializers
from .models import User, admin, Booking, startandentime, DiningPlace, DiningPlaceOperatingHours
from .serializers import UserSerializer, AdminSerializer, DiningPlaceSerializer, BookingSerializer, StartAndEndTimeSerializer, DiningPlaceOperatingHoursSerializer
from rest_framework.permissions import AllowAny
from passlib.hash import pbkdf2_sha256

# USER LOGIN
class UserLogin(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        encrypted_password = pbkdf2_sha256.hash(password)
        user = User.objects.filter(username=username).first()
        if user:  
            if pbkdf2_sha256.verify(password, encrypted_password):
                return Response({'token': user.token})
            else:
                return Response({'error': 'Invalid credentials'}, status=400)

# USER REGISTRATION
class RegisterUser(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            password = request.data.get('password')
            encrypted_password = pbkdf2_sha256.hash(password)
            serializer.save(password=encrypted_password)
            return Response({'status': 'Account successfully created', 'status_code': 200, 'user_id': serializer.data['id']})
        return Response(serializer.errors)
    
# ADMIN REGISTRATION
# ADMIN REGISTRATION
class RegisterAdmin(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            password = request.data.get('password')
            encrypted_password = pbkdf2_sha256.hash(password)
            serializer.save(password=encrypted_password)
            return Response({'status': 'Account successfully created', 'status_code': 200, 'admin_id': serializer.data['id']})
        return Response(serializer.errors)
    
# ADMIN LOGIN
class AdminLogin(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        encrypted_password = pbkdf2_sha256.hash(password)
        admin = admin.objects.filter(username=username).first()
        if admin:
            if pbkdf2_sha256.verify(password, encrypted_password):
                return Response({'token': admin.token})
            else:
                return Response({'error': 'Invalid credentials'}, status=400)
        return Response({'error': 'Invalid credentials'}, status=400)

class UserList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DinningPlaceList(APIView):

    def get(self, request):
        dinningplaces = DiningPlace.objects.all()
        serializer = DiningPlaceSerializer(dinningplaces, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiningPlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'{serializer.data["name"]} added successfully', 'place_id': serializer.data['id'], 'status_code': 200})
        return Response(serializer.errors)

class search(APIView):
    def get(self, request):
        search_query = request.query_params.get('name')
        if not search_query:
            return Response({'error': 'Search query parameter is missing'}, status=400)
        dinningplaces = DiningPlace.objects.filter(name__icontains=search_query)
        serializer = DiningPlaceSerializer(dinningplaces, many=True)
        return Response(serializer.data)
#  [GET] /api/dining-place?name={search_query}




class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    