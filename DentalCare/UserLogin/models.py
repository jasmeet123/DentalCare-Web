from __future__ import unicode_literals

from django.db import models
from dentist_login.models import Dentist


class UserLogin(models.Model):
    id = models.AutoField(primary_key=True);
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(max_length=50,blank=True,null=True)
    # profile_pic = models.ImageField(upload_to="profile_image",blank=True,null=True)
    gender = models.CharField(max_length=5,blank=True,null=True)
    fbuserId = models.CharField(max_length=50,default='1')
    age = models.IntegerField(blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=50,blank=True,null=True)
    zip = models.CharField(max_length=5,blank=True,null=True)
    enable = models.BooleanField(default=True)
    access_token = models.CharField(max_length=1000)
    login_type = models.CharField(max_length=20,blank=True,null=True)
    user_dentist = models.ForeignKey(Dentist, default= "", null= True)


    # owner = models.ForeignKey('User', blank=True, null=True, related_name='tips')

    def __str__(self):
        return self.first_name

    def save(self, *args,**kwargs):
        super(UserLogin,self).save(*args,**kwargs)
