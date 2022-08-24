from dataclasses import fields
from django.contrib import admin
from .models import student, staff, division, subject

# Description for sections
# Student
sPersonalInfo = "Text goes here"
sParentInfo = "Text goes here"
sContactInfo = "Text goes here"
sDepartmentInfo = "Text goes here"
sImageInfo = "Text goes here"

# Staff
stPersonalInfo = "Text goes here"
stContactInfo = "Text goes here"
stDepartmentInfo = "Text goes here"
stImageInfo = "Text goes here"

# Register your models here.
class divisionOption(admin.ModelAdmin):
    list_display = [
        'department'
    ]

class subjectOption(admin.ModelAdmin):
    list_display = [
        'topic'
    ]

class studentOption(admin.ModelAdmin):
    fieldsets = (
        ('Personal Info', {
            "fields": (
                ('firstName', 'lastName'),
                ('secondName', 'thirdName'),
                'dob'
            ),
            #"description" : '%s' % sPersonalInfo
        }),
        ("Parent's Info", {
            "fields": (
                ('fatherFirstName', 'fatherLastName'),
                'motherFullName'
            ),
            #"description" : '%s' % sParentInfo,
            'classes': ('collapse',),
        }),
        ("Contact Info", {
            "fields": (
                ('emailID', 'phoneNo'),
                'currentAddress',
                'permanentAddress'
            ),
            #"description" : '%s' % sContactInfo,
            'classes': ('collapse',),
        }),
        ("Department", {
            "fields": [
                'division'
            ],
            #"description" : '%s' % sDepartmentInfo,
            'classes': ('collapse',),
        }),
        ('Image', {
            'fields': [
                'avatar'
            ],
            #"description" : '%s' % sImageInfo,
            'classes': ('collapse',),
        })
    )
    
    list_display = [
        'firstName', 
        'lastName',
        'emailID',
        'phoneNo',
        'dob',
    ]
    list_filter = [
        'division',
        'joinDate'
    ]
    search_fields = ['firstName', 'lastName', 'secondName', 'thirdName', 'emailID', 'phoneNo',]

class staffOption(admin.ModelAdmin):
    fieldsets = (
        ('Personal Info', {
            "fields": (
                ('firstName', 'lastName'),
                'middleName'
            ),
            #"description" : '%s' % stPersonalInfo
        }),
        ('Department', {
            "fields": (
                'division',
                ('subjectsTaken', 'extras'),
                'yearsOfExperience'
            ),
            #"description" : '%s' % stDepartmentInfo,
            'classes': ('collapse',),
        }),
        ("Contact Info", {
            "fields": (
                ('emailID', 'phoneNo'),
                'currentAddress',
                'permanentAddress'
            ),
            #"description" : '%s' % stContactInfo,
            'classes': ('collapse',),
        }),
        ('Image', {
            'fields': [
                'avatar'
            ],
            #"description" : '%s' % stImageInfo,
            'classes': ('collapse',),
        })
    )
    list_display = [
        'firstName', 
        'lastName',
        'emailID',
        'phoneNo',
    ]
    list_filter = [
        'division',
        'subjectsTaken',
        'joinDate'
    ]
    search_fields = ['firstName', 'lastName', 'middleName', 'emailID', 'phoneNo',]
    
admin.site.register(student, studentOption)
admin.site.register(staff, staffOption)
admin.site.register(division)
admin.site.register(subject)