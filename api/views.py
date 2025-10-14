from django.shortcuts import render
from rest_framework.response import Response
from .models import role1,QA,Admin,accountent,product,product_details
from rest_framework import status
from .serializers  import role1Serializer,product_detailsSerializer
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
        
            
@api_view(['POST'])
def add_product_details(request):
    Company_name=request.data.get("Company_name")
    serial_number=request.data.get("serial_number")
    date=request.data.get("date")
    Customer_name=request.data.get("Customer_name")
    Customer_No=request.data.get("Customer_No")
    Customer_date=request.data.get("Customer_date")
    material_Description=request.data.get("material_Description")
    Quantity =request.data.get("Quantity")
    mobile =request.data.get("mobile")
    Remarks =request.data.get("Remarks")
    size=request.data.get("size")
    Thick=request.data.get("Thick")
    Grade=request.data.get("Grade")
    Drawing=request.data.get("Drawing")
    Test_Certificate=request.data.get("Test_Certificate")
    status=request.data.get("status")

    try:
        product_data=product_details.objects.create(
            Company_name=Company_name,
            serial_number=serial_number,
            date=date,
            Customer_name=Customer_name,
            Customer_No=Customer_No,
            Customer_date=Customer_date,
            material_Description=material_Description,
            Quantity=Quantity,
            mobile=mobile,
            Remarks=Remarks,
            size=size,
            Thick=Thick,
            Grade=Grade,
            Drawing=Drawing,
            Test_Certificate=Test_Certificate,
            status="pending"
        )
    except product_details.DoesNotExist:
        return Response({"msg":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
    return Response({
        "msg":"data added successfully",
        "Company_name":Company_name,
        "serial_number":serial_number,
        "date":date,
        "Customer_name":Customer_name,
        "Customer_No":Customer_No,
        "Customer_date":Customer_date,
        "material_Description":material_Description,
        "Quantity":Quantity,
        "mobile":mobile,
        "Remarks":Remarks,
        "size":size,
        "Thick":Thick,
        "Grade":Grade,
        "Drawing":Drawing,
        "Test_Certificate":Test_Certificate,
        "status":"pending"
    },status=200)


@api_view(['GET'])
def get_product_details(request):
    product_data=product_details.objects.all()
    serializer =product_detailsSerializer(product_data,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_product_status(request, id):
    product_instance = product_details.objects.get(id=id)

    if not product_instance:
        return Response({"msg": "No data found"}, status=status.HTTP_404_NOT_FOUND)
    
    product_instance.Company_name = request.data.get('Company_name', product_instance.Company_name)
    product_instance.serial_number = request.data.get('serial_number', product_instance.serial_number)
    product_instance.date = request.data.get('date', product_instance.date)
    product_instance.Customer_name = request.data.get('Customer_name', product_instance.Customer_name)
    product_instance.Customer_No = request.data.get('Customer_No', product_instance.Customer_No)
    product_instance.Customer_date = request.data.get('Customer_date', product_instance.Customer_date)
    product_instance.mobile = request.data.get('mobile', product_instance.mobile)
    product_instance.material_Description = request.data.get('material_Description', product_instance.material_Description)
    product_instance.Quantity=request.data.get('Quantity',product_instance.Quantity)
    product_instance.Remarks = request.data.get('Remarks', product_instance.Remarks)
    product_instance.size = request.data.get('size', product_instance.size)
    product_instance.Thick = request.data.get('Thick', product_instance.Thick)
    product_instance.Grade = request.data.get('Grade', product_instance.Grade)
    product_instance.Drawing = request.data.get('Drawing', product_instance.Drawing)
    product_instance.Test_Certificate = request.data.get('Test_Certificate', product_instance.Test_Certificate)
    product_instance.status = request.data.get('status', product_instance.status)
    product_instance.save()
    serializer = product_detailsSerializer(product_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

    

@api_view(['DELETE'])
def delete_product(request, id):
    product_instance = product_details.objects.get(id=id).delete()

    if not product_instance:
        return Response({"msg": "No data found"}, status=status.HTTP_404_NOT_FOUND)
    
    return Response({"msg": "data deleted"}, status=status.HTTP_200_OK)