from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin 
from django.db import models
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(_("email address"), unique=True)

        objects = CustomUserManager()

   
    

