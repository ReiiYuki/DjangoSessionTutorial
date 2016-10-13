from django.db import models

class Users(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    middlename = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    dateofB = models.CharField(max_length=45)

    class Meta:
        db_table = "person"

class Administrator(models.Model):
    num = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    class Meta:
        db_table = "administrator"
