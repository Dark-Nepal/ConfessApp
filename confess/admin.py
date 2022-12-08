from django.contrib import admin
from .models import confess

class confessadmin(admin.ModelAdmin):
    list_display = ( 'confession', 'post_date')
    ordering = ['-post_date',]


admin.site.register(confess,confessadmin)

