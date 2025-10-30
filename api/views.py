from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from api.serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # Izinkan siapa saja (tanpa login) untuk akses
    serializer_class = UserSerializer

class GetUserAllView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# class GetUserAllView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer