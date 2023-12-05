from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    REQUIRED_FIELDS = []
    class Meta:
        db_table = 'custom_user'
