from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, name, email, tc, password=None,password2=None):
        """
        Creates and saves a User with the given name, email, tc and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        if not name:
            raise ValueError("Users must have a name")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, tc, password=None,password2=None):
        """
        Creates and saves a superuser with the given name, email, tc and password.
        """
        user = self.create_user(
            name=name,
            email=email,
            tc=tc,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
#cutom user model 
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = MyUserManager()  

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always for admin
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always for admin
        return self.is_admin

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # All admins are staff
        return self.is_admin