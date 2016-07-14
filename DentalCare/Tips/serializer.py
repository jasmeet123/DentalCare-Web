from rest_framework import serializers
from models import Tip
from django.contrib.auth.models import  User

class TipsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Tip
        fields = ('id','title','desc','image', 'date','owner')
