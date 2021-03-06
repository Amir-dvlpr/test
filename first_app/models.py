from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

       user = models.OneToOneField(User, on_delete = models.PROTECT)

       profile_site = models.URLField(blank = True)
       profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)


       def __str__(self):
              return self.user.username


class User1(models.Model):
       first_name = models.CharField(max_length = 128)
       last_name = models.CharField(max_length = 128)
       email = models.EmailField(max_length = 256, unique = True)


# Create your models here.
