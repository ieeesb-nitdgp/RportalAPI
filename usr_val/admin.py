from django.contrib import admin
from .models import Student, Teacher, ResearchStatement

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(ResearchStatement)
