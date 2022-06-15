from django.db import models

class re_User(models.Model):
    id = models.BigIntegerField
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    alternatePhone = models.CharField(max_length=255, default="unavailable")
    pan = models.CharField(max_length=255)
    aadhar = models.CharField(max_length=255)
    createDate = models.CharField(max_length=255)
    userType = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default= True)



    