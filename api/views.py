from django.shortcuts import render
from rest_framework.response import Response
from .models import role1,QA,Admin,accountent,product
from rest_framework import status
from .serializers  import role1Serializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def single_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    role_type = request.data.get("role_type")

    if not username or not password or not role_type:
        return Response("user not found")
    try:
        if role_type == "role1":
            role1_login = role1.objects.get(username=username,password=password,role_type=role_type)
        elif role_type == "QA":
            Qa_login = QA.objects.get(username=username,password=password,role_type=role_type)
        elif role_type == "product":
            product_login = product.objects.get(username=username,password=password,role_type=role_type)
        elif role_type == "Admin":
            Admin_login = Admin.objects.get(username=username,password=password,role_type=role_type)
        elif role_type == "accountent":
            accountent_login = accountent.objects.get(username=username,password=password,role_type=role_type)
        else:
            return Response({"msg":"invalid user"})
        
    except (role1.DoesNotExist, QA.DoesNotExist, product.DoesNotExist,
            Admin.DoesNotExist, accountent.DoesNotExist):
        return Response({"msg": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)

    # Login successful
    return Response({
        "msg": "Login successful",
        "username": username,
        "role_type": role_type
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_data(request):
    get_data =role1.objects.all()

    get=[]
    for gets in get_data:
        get.append({
            "username":gets.username,
            "password":gets.password,
        })
    return Response(get)