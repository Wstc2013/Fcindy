# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=32, verbose_name='部门', null=True)

class UserProfile(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名', null=True)
    user = models.OneToOneField(User)
    department = models.ForeignKey(Department)
    phone = models.CharField(max_length=11, null=True, verbose_name='电话')