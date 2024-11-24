# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")
        
        # Normalize the email (lowercase domain part)
        email = self.normalize_email(email)

        # Create the user object
        user = self.model(email=email, name=name)
        
        # Hash and set the password
        user.set_password(password)
        
        # Save the user to the database
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, name, password):
        """Create and return a new superuser"""
        user = self.create_user(email, name, password)
        user.is_superuser = True  # Provided by PermissionsMixin
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()  # Custom manager (defined later)
    
    USERNAME_FIELD = 'email'  # Email replaces the username for authentication
    REQUIRED_FIELDS = ['name']  # Fields required during user creation

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of the user"""
        return self.email
