from django.contrib import admin
from hrs.models import Hr,Employee
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Employee)
admin.site.register(Hr, UserAdmin)