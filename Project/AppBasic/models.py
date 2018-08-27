from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Your_Website = models.CharField(blank=True,max_length = 64)
    Profile_Pic = models.ImageField(upload_to = 'uploaded_pics',blank=True)

    def __str__(self):
        return self.user.username
####################################################

class DataModel(models.Model):
    Select_Your_Image = models.ImageField(upload_to = 'userpost_data',blank = True)
    Description = models.CharField(max_length = 1024)


