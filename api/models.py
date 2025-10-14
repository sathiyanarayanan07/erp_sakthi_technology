from django.db import models

# Create your models here.
class role1(models.Model):

    username = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    role_type = models.CharField(max_length=10,default="role1")

    def __str__(self):
        return f"{self.username} -{self.password}"
    
class QA(models.Model):

    username = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    role_type = models.CharField(max_length=10,default="QA")

    def __str__(self):
        return f"{self.username} -{self.password}"

    
class product(models.Model):

    username = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    role_type = models.CharField(max_length=10,default="product")

    def __str__(self):
        return f"{self.username} -{self.password}"
    
    
class accountent(models.Model):

    username = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    role_type = models.CharField(max_length=10,default="accountent")

    def __str__(self):
        return f"{self.username} -{self.password}"
    
    
class Admin(models.Model):

    username = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    role_type = models.CharField(max_length=10,default="Admin")

    def __str__(self):
        return f"{self.username} -{self.password}"
    
class product_details(models.Model):

    Company_name = models.CharField(max_length=30,null=True,blank=True)
    serial_number = models.CharField(max_length=30,null=True,blank=True)
    date=models.DateField(auto_now_add=True)
    Customer_name = models.CharField(max_length=30,null=True,blank=True)
    Customer_No = models.CharField(max_length=30,null=True,blank=True)
    Customer_date = models.DateField(null=True,blank=True)
    mobile = models.CharField(max_length=30,null=True,blank=True)
    material_Description = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.CharField(max_length=30,null=True,blank=True)
    Remarks = models.CharField(max_length=100,null=True,blank=True)
    size=models.BooleanField(default=False)
    Thick=models.BooleanField(default=False)
    Grade=models.BooleanField(default=False)
    Drawing=models.BooleanField(default=False)
    Test_Certificate=models.BooleanField(default=False)
    status=models.CharField(max_length=30,default="pending")

    def __str__(self):
        return f"{self.Company_name} -{self.serial_number}"