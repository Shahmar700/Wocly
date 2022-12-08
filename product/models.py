from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from product.helper import seo
from django.urls import reverse
from accounts.models import MyUser
from ckeditor.fields import RichTextField
from .options import *
from accounts.models import *

User = get_user_model()

# Create your models here.
class AdsSettings(models.Model):
    ad1_image=models.ImageField(verbose_name="Ad1 Image",upload_to="ads",null=True)
    link1 = models.CharField(verbose_name="Link 1",max_length=1500,null=True)
    ad2_image=models.ImageField(verbose_name="Ad2 Image",upload_to="ads",null=True)
    link2 = models.CharField(verbose_name="Link 2",max_length=1500,null=True)
    ad3_image=models.ImageField(verbose_name="Ad3 Image",upload_to="ads",null=True)
    link3 = models.CharField(verbose_name="Link 3",max_length=1500,null=True)
    ad4_image=models.ImageField(verbose_name="Ad4 Image",upload_to="ads",null=True)
    link4 = models.CharField(verbose_name="Link 4",max_length=1500,null=True)

    
    
    


    def __str__(self):
        return "AdsSettings"
    

class Brand(models.Model):
    name = models.CharField(verbose_name="Brand name",max_length=50)

    def __str__(self):
        return self.name
    

class MainCategory(models.Model):
    name = models.CharField(verbose_name="Category Name",max_length=50)
    slug = models.SlugField(verbose_name="Slug",editable=False,unique=True)
    image = models.ImageField(verbose_name="Image",null =True,upload_to="category_img")

    ad1_image=models.ImageField(verbose_name="Ad1 Image",upload_to="ads",null=True)
    link1 = models.CharField(verbose_name="Link 1",max_length=1500,null=True)
    ad2_image=models.ImageField(verbose_name="Ad2 Image",upload_to="ads",null=True)
    link2 = models.CharField(verbose_name="Link 2",max_length=1500,null=True)
    ad3_image=models.ImageField(verbose_name="Ad3 Image",upload_to="ads",null=True)
    link3 = models.CharField(verbose_name="Link 3",max_length=1500,null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Category"
        verbose_name_plural ="Categories"

    def save(self, *args, **kwargs):
        super(MainCategory, self).save(*args, **kwargs)
        self.slug = seo(self.name)
        super(MainCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:category_detail', kwargs={'slug': self.slug})


    
class SubCategory(models.Model):
    name = models.CharField(verbose_name="Sub Category Name", max_length=50)
    slug = models.SlugField(verbose_name="Slug",editable=False,unique=True)
    category = models.ForeignKey(MainCategory,verbose_name="Choose Category",on_delete=models.CASCADE,related_name="category")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Sub Category"
        verbose_name_plural ="Sub Categories"

    def save(self, *args, **kwargs):
        super(SubCategory, self).save(*args, **kwargs)
        self.slug = seo(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:category_detail', kwargs={'slug': self.slug})




    




class Product(models.Model):
    seller = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,verbose_name="seller")
    name = models.CharField(verbose_name="Product Name",max_length=50)
    description = RichTextField(verbose_name="About Product")
    mini_description = RichTextField(verbose_name="Mini Decription",null=True)
    price = models.FloatField(verbose_name="Price")
    tempamount = models.FloatField(default=1)


    category = models.ForeignKey(SubCategory,null=True,verbose_name="Sub Category",on_delete=models.CASCADE,related_name="sub_category")
    brand = models.ForeignKey(Brand,null=True,verbose_name="Brand",on_delete=models.CASCADE,related_name="product_brand")

    slug = models.SlugField(editable=False, verbose_name="Slug",unique=True)
    
    draft = models.BooleanField(verbose_name="Shared",default=True)
    created_date = models.DateTimeField(verbose_name="Created Date",auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Updated_Date",auto_now=True)
    discount_percent = models.FloatField(default=0)
    sold = models.IntegerField(default=0)

    #not requiered
    color = models.CharField(max_length=200,verbose_name="Rengleri Daxil Edin :",null=True,blank=True)
    style = models.CharField(max_length=200,verbose_name="Style Elave Edin :",null=True,blank=True)
    wireless = models.IntegerField(choices=ANSWERTYPE,verbose_name="Wireless",null=True,blank=True)
    dimensions = models.CharField(max_length=200,verbose_name="Olculeri",null=True,blank=True)
    weight = models.IntegerField(null=True,verbose_name="Weight",blank=True)
    battery_life = models.CharField(max_length=100,verbose_name="Battery Life",null=True,blank=True)
    bluetooth = models.IntegerField(choices=ANSWERTYPE,null=True,blank=True)
    

    #wishlist
    wishlist = models.ManyToManyField(User,related_name="wishlist",blank=True,null=True)
    basket = models.ManyToManyField(User,related_name="basket",blank=True,null=True)

    
    @property
    def discount(self):
        if self.discount_percent > 0:
            discounted_price = self.price - self.price*self.discount_percent/100
            return discounted_price
        return self.price


    def __str__(self):
        return self.name

    def main_product_image(self):
        product_images = ProductImage.objects.filter(product=self)
        if product_images.exists():
            return product_images.first().image.url
        return '-'

    class Meta:
        verbose_name ="Product"
        verbose_name_plural ="Products"

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        self.slug = seo(self.name)+str(self.seller.id)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product:product_detail', kwargs={"slug": self.slug})



class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="Images")
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return self.product.name or self.product.slug
    
    
    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"


class Basket(models.Model):
    product = models.ForeignKey(Product,related_name="basket_product" ,on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="basket_user" ,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

    class Meta:
        ordering = ("-id",)
        verbose_name = "Basket"
        verbose_name_plural = "Basket"


    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
  ('Accepted','Accepted'),
  ('Packed','Packed'),
  ('On The Way','On The Way'),
  ('Delivered','Delivered'),
  ('Cancel','Cancel')
)

class Invoice(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "invoice_user")
 customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "invoice_customer")
 product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "invoice_product")
 quantity = models.PositiveIntegerField(default=1)
 ordered_date = models.DateTimeField(auto_now_add=True)
 status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

  # Below Property will be used by orders.html page to show total cost
 @property
 def total_cost(self):
   return self.quantity * self.product.discount

class Notification(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name = "notification_user")
    content = models.TextField()


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product,related_name="comments",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.email

