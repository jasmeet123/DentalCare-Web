from rest_framework import serializers
from .models import Request

class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('request_title','request_desc','request_user','request_dentist')

    def update(self, instance, validated_data):

        instance.request_title = validated_data.get('request_title', instance.request_title)
        instance.request_desc = validated_data.get('request_desc', instance.request_desc)
        instance.request_user = validated_data.get('request_user', instance.request_user)
        instance.request_dentist = validated_data.get('request_dentist', instance.request_dentist)
        instance.save()
        return instance