from django.shortcuts import render
from rest_framework.response import Response
from .models import role1
from rest_framework import status
from .serializers  import role1Serializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def role1_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response("user not found")
    
    login = role1.objects.get(
        username= username,
        password =password,
    )
    login.save()

    return Response ({"login successfully"},status=200)