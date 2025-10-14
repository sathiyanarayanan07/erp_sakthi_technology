from django.db import models

# Create your models here.
class role1(models.Model):
    username = models.CharField(max_length=30,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return f"{self.username} -{self.password}"
