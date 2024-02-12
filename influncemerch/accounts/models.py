from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin 
from django.db import models
from .managers import CustomUserManager
from django.utils import timezone
import uuid 
import hashlib

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
        date_joined = models.DateTimeField(default=timezone.now)
        last_login = models.DateTimeField(null=True)

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

   
    

