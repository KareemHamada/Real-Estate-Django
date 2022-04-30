from django.db import models
from django.contrib.auth.models import User



class Building(models.Model):
    publisher = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    type = models.CharField(max_length=20)
    
    forwhat = models.CharField(max_length=20) 

    area = models.IntegerField(null=False,blank=False)
    rooms = models.CharField(max_length=20,null=True,blank=True) 
    price = models.IntegerField()
    bathroom = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length = 200,null=False,blank=False)
    images = models.ImageField(null=True,blank=True,upload_to="images/")
    # image2 = models.ImageField(null=True,blank=True,upload_to="images/")
    # image3 = models.ImageField(null=True,blank=True,upload_to="images/")
    # image4 = models.ImageField(null=True,blank=True,upload_to="images/")
    # image5 = models.ImageField(null=True,blank=True,upload_to="images/")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.type