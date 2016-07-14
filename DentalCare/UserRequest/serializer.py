from rest_framework import serializers
from .models import Request

class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('request_title','request_desc','request_user','request_dentist')