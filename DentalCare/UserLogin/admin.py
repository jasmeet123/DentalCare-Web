from django.contrib import admin
from .models import UserLogin


class UserLoginAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name','email','fbuserId','gender','age','city','state','country','zip','enable','access_token','login_type','user_dentist']

admin.site.register(UserLogin, UserLoginAdmin)
