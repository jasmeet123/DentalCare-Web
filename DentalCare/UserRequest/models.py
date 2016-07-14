from __future__ import unicode_literals

from django.db import models
from dentist_login.models import Dentist


class Request(models.Model):
    id = models.AutoField(primary_key=True);
    request_title = models.CharField(max_length=50, null= True)
    request_desc = models.CharField(max_length=1500)
    request_user  = models.EmailField(max_length=50)
    request_dentist = models.ForeignKey(Dentist, default= "", null= True)

    # owner = models.ForeignKey('User', blank=True, null=True, related_name='tips')

    def __str__(self):
        return self.request_title

    def save(self, *args,**kwargs):
        super(Request,self).save(*args,**kwargs)
