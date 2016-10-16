from django.db import models

# Create your models here.
class User(models.Model) :
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    firstName= models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    dateOfBirth = models.DateField(null=True,blank=True)
    favouriteColor = models.CharField(max_length=20)
    class Meta :
        db_table = 'user'
