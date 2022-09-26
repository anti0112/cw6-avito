from distutils.command.upload import upload
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    ADMIN = 'admin'
    USER = 'user'
    ROLE = [(ADMIN, 'admin'), (USER, 'user')]


class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True)
    role = models.CharField(choices=UserRoles.ROLE, default=UserRoles.USER, max_length=50)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]
    objects = UserManager()
    
    @property
    def is_superuser(self):
        return self.is_admin
    
    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def has_perm(self):
        return self.is_admin
    
    @property
    def has_modules_perm(self):
        return self.is_admin
    
    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN # 

    @property
    def is_user(self):
        return self.role == UserRoles.USER
    