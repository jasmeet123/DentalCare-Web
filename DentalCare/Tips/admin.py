from django.contrib import admin

from .models import Tip


class TipsAdmin(admin.ModelAdmin):
    fields = ['title','desc','image','owner']

admin.site.register(Tip, TipsAdmin)
