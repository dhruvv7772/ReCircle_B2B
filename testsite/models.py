from django.db import models

class re_user(models.Model):
    name = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=255, null=True)
    alternatePhone = models.CharField(max_length=255, null=True, default="unavailable")
    pan = models.CharField(max_length=255,null=True)
    aadhar = models.CharField(max_length=255,null=True)
    createDate = models.CharField(max_length=255,null=True)
    userType = models.CharField(max_length=255,null=True)
    active = models.BooleanField(default= True,null=True)
    password = models.CharField(max_length=255,default=True, null=True)

class admin_Details(models.Model):
    username=models.CharField(max_length=25, null=True)
    password=models.CharField(max_length=10, null=True)


# class Meta:
#     db_table="re_user"
    