from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
import re
Email_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
Password_Regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
Name_Regex = re.compile(r'^[a-zA-Z]*$')

class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm_password):
        errors = []
        if len(first_name) < 2:
            errors.append('First name must be longer than 2 characters')
        if not Name_Regex.match(first_name):
            errors.append('First name cannot have numbers')
        if len(last_name) < 2:
            errors.append('Last name must be longer than 2 characters')
        if not Name_Regex.match(last_name):
            errors.append('Last name cannot have numbers')
        if len(email) == 0:
            errors.append('Please enter an email address')
        if not Email_Regex.match(email):
            errors.append('Please enter a valid email address')
        if len(password) == 0:
            errors.append('Please enter a password')
        if not Password_Regex.match(password):
            errors.append('Password must contain at least one lowercase letter, one uppercase letter, and one digit')
        if not (password) == (confirm_password):
            errors.append('Password and confirm password must be the same')
        if not len(errors) == 0:
            return (False, errors)
        else:
            password = str(password)
            pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
            user = User.Usermgr.create(first_name = first_name, last_name = last_name, email = email, password = pw_hash)
            return (True, user)

    def login(self, email, password):
        errors = []
        if len(email) == 0:
            errors.append('Please enter an email address')
        if not Email_Regex.match(email):
            errors.append('Please enter a valid email address')
        if len(password) == 0:
            errors.append('Please enter a password')
        if not Password_Regex.match(password):
            errors.append('Password must contain at least one lowercase letter, one uppercase letter, and one digit')
        if not len(errors) == 0:
            return (False, errors)
        else:
            user = User.Usermgr.filter(email = email)
            user_password = user[0].password
            if bcrypt.hashpw(str(password), str(user_password)) == user_password:
                return (True, user)
            else:
                errors.append('Password is incorrect!')
                return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    Usermgr = UserManager()
