from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    email = models.EmailField()
    message = models.CharField(max_length=1200)

    has_read = models.BooleanField(default=False)
