from rest_framework import serializers
from .models import UserLogin

class UserLoginSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user_dentist.email')
    class Meta:
        model = UserLogin
        fields = ('id','first_name','last_name','email','fbuserId','gender','age','city','state','country','zip','enable','access_token','login_type','owner')

    def update(self, instance, validated_data):

        instance.enable = validated_data.get('enable', instance.enable)
        instance.save()
        return instance
