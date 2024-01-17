from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()


class Profile(models.Model):
    u_name = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(unique=True)
    aadhar_number = models.CharField(max_length=12, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self) -> str:
        return "Profile object"
