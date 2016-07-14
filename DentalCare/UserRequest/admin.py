from django.contrib import admin
from .models import Request

# Register your models here.
class UserRequestAdmin(admin.ModelAdmin):
    fields = ['request_title','request_desc','request_user']

admin.site.register(Request, UserRequestAdmin)
