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

@api_view(['POST'])
def single_signup(request):
    username =request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    role_type =request.data.get("role_type")



    email_exists = (
        role1.objects.filter(email=email).exists() or
        QA.objects.filter(email=email).exists() or
        product.objects.filter(email=email).exists() or
        Admin.objects.filter(email=email).exists() or
        accountent.objects.filter(email=email).exists()
    )

    if email_exists:
        return Response({"msg": "Email already exists"}, status=400)
 
    try:
        if role_type =="role1":
            role = role1.objects.create(username=username,email=email,password=password,role_type=role_type)
        elif role_type == "QA":
            role2 = QA.objects.create(username=username,email=email,password=password,role_type=role_type)
        elif role_type == "product":
            role3 = product.objects.create(username=username,email=email,password=password,role_type=role_type)
        elif role_type == "Admin":
            role2 = Admin.objects.create(username=username,email=email,password=password,role_type=role_type)
        elif role_type == "accountent":
            role2 = accountent.objects.create(username=username,email=email,password=password,role_type=role_type)
        else:
            return Response({"msg":"invaild data"},status=200)
        
    except (role1.DoesNotExist, QA.DoesNotExist, product.DoesNotExist,
            Admin.DoesNotExist, accountent.DoesNotExist):
        return Response({"msg": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)

    # Login successful
    return Response({
        "msg": "signup successful",
        "username": username,
        "email":email,
        "password":password,
        "role_type": role_type
    }, status=200 )   
        
            
