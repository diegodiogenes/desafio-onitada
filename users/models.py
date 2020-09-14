from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User Model
    """
    # fields
    name = models.CharField("Name", max_length=255, help_text="Fullname of the Client")
    cpf = models.CharField("CPF", unique=True, max_length=14, help_text="Valid CPF of the Client")
    email = models.EmailField("Email", unique=True, help_text="Email of the Client")

    class Meta:
        ordering = ['id']
