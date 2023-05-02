from django.db import models

# Create your models here.


class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE, null=True)
    password = models.CharField(max_length=255, default='-')
    email = models.EmailField()
    phone = models.CharField(max_length=255)



