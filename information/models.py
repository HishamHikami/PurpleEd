from __future__ import division
from django.contrib import admin
from django.db import models
from datetime import datetime
import os
from django.core.validators import RegexValidator

def cfn_student(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s_%s.%s" % (instance.firstName, instance.department, str(instance.joinDate), ext)
    return os.path.join('uploads/images/students', filename)

class division(models.Model):
    department = models.CharField(max_length=30)

    @admin.display(
        ordering='department',
    )

    def __str__(self):
        return self.department

class student(models.Model):
    firstName = models.CharField(max_length=36)
    secondName = models.CharField(max_length=36, null=True, blank=True)
    thirdName = models.CharField(max_length=36, null=True, blank=True)
    lastName = models.CharField(max_length=36, null=True, blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    division = models.ManyToManyField(division, blank=True)
    emailID = models.EmailField(max_length=68, null=True, blank=True)
    phoneRegex = RegexValidator(regex="(\+\d{1,3})?,?\s?\d{8,13}", message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.")
    phoneNo = models.CharField(validators=[phoneRegex], max_length=17, null=True, blank=True)
    currentAddress = models.CharField(max_length=80, null=True, blank=True)
    permanentAddress = models.CharField(max_length=80, null=True, blank=True)
    fatherFirstName = models.CharField(max_length=36, null=True, blank=True)
    fatherLastName = models.CharField(max_length=36, null=True, blank=True)
    motherFullName = models.CharField(max_length=36, null=True, blank=True)
    avatar = models.ImageField(upload_to=cfn_student, null=True, blank=True)
    joinDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    @admin.display(
        ordering='modified',
    )

    def __str__(self):
        return self.firstName

def cfn_staff(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s_%s.%s" % (instance.firstName, instance.department, str(instance.joinDate), ext)
    return os.path.join('uploads/images/staffs', filename)

class subject(models.Model):
    topic = models.CharField(max_length=50)

    @admin.display(
        ordering='topic',
    )

    def __str__(self):
        return self.topic

class staff(models.Model):
    firstName = models.CharField(max_length=36)
    middleName = models.CharField(max_length=36, null=True, blank=True)
    lastName = models.CharField(max_length=36, null=True, blank=True)
    division = models.ManyToManyField('division', blank=True)
    subjectsTaken = models.ManyToManyField('subject', blank=True)
    yearsOfExperience = models.IntegerField(null=True, blank=True)
    extras = models.CharField(max_length=110, null=True, blank=True)
    emailID = models.EmailField(max_length=68, null=True, blank=True)
    phoneRegex = RegexValidator(regex='^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.")
    phoneNo = models.CharField(validators=[phoneRegex], max_length=17, null=True, blank=True)
    currentAddress = models.CharField(max_length=80, null=True, blank=True)
    permanentAddress = models.CharField(max_length=80, null=True, blank=True)
    avatar = models.ImageField(upload_to=cfn_staff, null=True, blank=True)
    joinDate = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @admin.display(
        ordering='modified',
    )

    def __str__(self):
        return self.firstName

# Here are some help
# help_text="This is a help text"