from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
import requests



class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# def post(request):
#     url=""
#     headers={}
#     if request.method=="POST":
#         data=request.data
#         response=requests.post(url,headers=headers,data=data)
#         data=response.json()
#         return data
