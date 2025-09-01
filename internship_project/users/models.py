from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Use email as unique identifier (username stays for compatibility)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # username still required by AbstractUser

    def __str__(self):
        return self.email
