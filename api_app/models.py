from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # By setting related_name, we avoid clashes with the default auth.User model
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Custom related_name
        blank=True
    )