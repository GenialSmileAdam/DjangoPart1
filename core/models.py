from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any custom fields if they exist in the database
    # For now, just use the default fields from AbstractUser
    pass