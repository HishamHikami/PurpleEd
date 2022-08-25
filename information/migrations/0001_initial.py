# Generated by Django 3.2.13 on 2022-08-13 03:58

import django.core.validators
from django.db import migrations, models
import information.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=36)),
                ('secondName', models.CharField(blank=True, max_length=36, null=True)),
                ('thirdName', models.CharField(blank=True, max_length=36, null=True)),
                ('lastName', models.CharField(blank=True, max_length=36, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('emailID', models.EmailField(blank=True, max_length=68, null=True)),
                ('phoneNo', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.", regex='(\\+\\d{1,3})?,?\\s?\\d{8,13}')])),
                ('currentAddress', models.CharField(blank=True, max_length=80, null=True)),
                ('permanentAddress', models.CharField(blank=True, max_length=80, null=True)),
                ('fatherFirstName', models.CharField(blank=True, max_length=36, null=True)),
                ('fatherLastName', models.CharField(blank=True, max_length=36, null=True)),
                ('motherFullName', models.CharField(blank=True, max_length=36, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=information.models.cfn_student)),
                ('joinDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('division', models.ManyToManyField(blank=True, to='information.division')),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=36)),
                ('middleName', models.CharField(blank=True, max_length=36, null=True)),
                ('lastName', models.CharField(blank=True, max_length=36, null=True)),
                ('yearsOfExperience', models.IntegerField(blank=True, null=True)),
                ('extras', models.CharField(blank=True, max_length=110, null=True)),
                ('emailID', models.EmailField(blank=True, max_length=68, null=True)),
                ('phoneNo', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.", regex='^(\\+\\d{1,3})?,?\\s?\\d{8,13}')])),
                ('currentAddress', models.CharField(blank=True, max_length=80, null=True)),
                ('permanentAddress', models.CharField(blank=True, max_length=80, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=information.models.cfn_staff)),
                ('joinDate', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('division', models.ManyToManyField(blank=True, to='information.division')),
                ('subjectsTaken', models.ManyToManyField(blank=True, to='information.subject')),
            ],
        ),
    ]