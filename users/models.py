from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import MyUser


# Create your models here.


class Vendor(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to="Vendor_Img",null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    seller = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name="seller_vendor")
    street_1 = models.CharField(max_length=200,null=True,blank=True)
    street_2 = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    zip = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=100,null=True,blank=True)




    

    def __str__(self):
        return self.name
    