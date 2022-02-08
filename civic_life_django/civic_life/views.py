#from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, LegislationSerializer, ActionSerializer
from .models import User, Legislation, Action

# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LegislationList(generics.ListCreateAPIView):
    queryset = Legislation.objects.all()
    serializer_class = LegislationSerializer


class ActionList(generics.ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class LegislationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Legislation.objects.all()
    serializer_class = LegislationSerializer


class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
