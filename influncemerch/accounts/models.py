from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin 
from django.db import models
from .managers import CustomUserManager
from django.utils import timezone
import uuid 
import hashlib
from django.urls import reverse


GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
class User(AbstractBaseUser, PermissionsMixin):
        id = models.AutoField(primary_key=True)
        u_id =models.UUIDField(default=uuid.uuid4, editable=False)
        hashed_id = models.CharField(max_length=32,  unique=True, editable =False)
        first_name=models.CharField(max_length=32)
        last_name=models.CharField(max_length=32)
        email = models.EmailField(verbose_name="email address", unique=True)
        date_of_birth = models.DateTimeField(blank=True,null=True)
        picture = models.ImageField(blank=True, null=True)
        phone_number = models.CharField(max_length=10,unique=True)
        gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
        address= models.CharField(max_length=100)
        last_login = models.DateTimeField(null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)


        objects = CustomUserManager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS =['first_name','last_name','phone_number','address']

        def save(self, *args, **kwargs):
        # Hash the incremental_id using SHA-256
                hashed_id = hashlib.sha256(str(self.id).encode('utf-8')).hexdigest()
                self.hashed_id = hashed_id
                super().save(*args, **kwargs)

        def get_full_name(self):
                return self.first_name + ' ' +self.last_name
        
        def get_address(self):
                return self.address


class Category(models.Model):
        cat_id=models.AutoField(primary_key=True)
        title=models.CharField(max_length=64)
        description = models.CharField(max_length=100)
        url_slug=models.CharField(max_length=255)
        thumbnail=models.FileField()
        created_at=models.DateTimeField(auto_now_add=True)

        @staticmethod
        def get_all_category(self):
                return Category.objects.all()
        
        def __str__(self):
                return self.title
        
class SubCategories(models.Model):
        id=models.AutoField(primary_key=True)
        category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
        title=models.CharField(max_length=255)
        url_slug=models.CharField(max_length=255)
        thumbnail=models.FileField()
        description=models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)

        def get_absolute_url(self):
                return reverse("sub_category_list")

class Product(models.Model):
        id=models.AutoField(primary_key=True)
        url_slug=models.CharField(max_length=255)
        subcategories_id=models.ForeignKey(SubCategories,on_delete=models.CASCADE)
        product_name=models.CharField(max_length=255)
        brand=models.CharField(max_length=255)
        product_max_price=models.CharField(max_length=255)
        product_discount_price=models.CharField(max_length=255)
        product_description=models.TextField()
        product_long_description=models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)
        in_stock_total=models.IntegerField(default=1)
   
    

