# -*- coding: utf-8 -*-
from django.contrib import admin
from models import People, Professor, Student, Subject, Group, PageLaboratoryWork, MadeLaboratoryWork, LabComment
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from registration.models import RegistrationProfile
'''
class UserInline(admin.StackedInline):
    model = User
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    inlines = [UserInline]

admin.site.register(Student, StudentAdmin)
'''

'''
class UserInline(admin.StackedInline):
    model = User
    extra = 1

class PeopleAdmin(admin.ModelAdmin):
    inlines = [UserInline]

admin.site.register(People, PeopleAdmin)
'''


    
    
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Group)
admin.site.register(PageLaboratoryWork)
admin.site.register(MadeLaboratoryWork)
admin.site.register(LabComment)
#admin.site.register(RegistrationProfile)
admin.site.unregister(User)

class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )

admin.site.register(User, MyUserAdmin)
