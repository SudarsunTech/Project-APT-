from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, exams, Courses, Subjects, Summary, Report

# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)
admin.site.register(AdminHOD)
admin.site.register(exams)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Summary)
admin.site.register(Report)


