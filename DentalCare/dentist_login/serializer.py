from rest_framework import serializers
from .models import Dentist
from django.contrib.auth.models import  User

class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = ('id','zip','first_name','last_name','address','city','state','active','image','qualification','email','date_of_birth','is_active', 'is_admin')