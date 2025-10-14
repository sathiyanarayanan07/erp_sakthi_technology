from django.db import models

# Create your models here.
class role1(models.Model):

    username = models.CharField(max_length=30,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    role_type = models.CharField(max_length=10,default="role1")

    def __str__(self):
        return f"{self.username} -{self.password}"
    
class QA(models.Model):

    username = models.CharField(max_length=30,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    role_type = models.CharField(max_length=10,default="QA")

    def __str__(self):
        return f"{self.username} -{self.password}"

    
class product(models.Model):

    username = models.CharField(max_length=30,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    role_type = models.CharField(max_length=10,default="product")

    def __str__(self):
        return f"{self.username} -{self.password}"
    
    
class accountent(models.Model):

    username = models.CharField(max_length=30,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    role_type = models.CharField(max_length=10,default="accountent")

    def __str__(self):
        return f"{self.username} -{self.password}"
    
    
class Admin(models.Model):

    username = models.CharField(max_length=30,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    role_type = models.CharField(max_length=10,default="Admin")

    def __str__(self):
        return f"{self.username} -{self.password}"