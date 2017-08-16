# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "User First Name should not be empty"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "User Last Name should not be empty"
        if len(postData['email']) < 1:
            errors["email"] = "User Email should not be empty"
        return errors;
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: first_name = {} last_name = {} email = {}>".format(self.first_name, self.last_name, self.email)