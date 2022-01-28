from django.db import models
import re
import bcrypt

class Validator(models.Manager):
    def validate_reg(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 1:
            errors['first_name'] = "First name is requires!"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Last name is required!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['email']) < 1:
            errors['email'] = "Email is required!"
        if len(postData['password']) < 1:
            errors['password'] = "Password is required!"
        if postData['password'] != postData['pass_confirm']: 
            errors['password'] = "Password and password confirm do not match!"
        return errors

    def validate_login(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            log_user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(), log_user.password.encode()):
                errors['password'] = "Invalid login attempt"
        else:
            errors['password'] = 'Invalid login attempt'
        return errors

    def validate_update(self, postData):
        errors = {}
        # entered_email = postData['email']
        # test = User.objects.filter(email = entered_email)
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 1:
            errors['first_name'] = "First name is requires!"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Last name is required!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        # if test.email:
        #     errors['email'] = "This email already exists, Please re-enter"
        return errors

    def validate_quote(self, postData):
        errors = {}
        if len(postData['author']) < 4:
            errors['author'] = "Author's name has to be more than 3 characters.Please re-enter"
        if len(postData['quotes']) < 11:
            errors['quotes'] = "The quote needs to be more than 10 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255) 
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validator()

class Quote(models.Model):
    author_name = models.CharField(max_length = 45)
    quote = models.TextField()
    likes = models.IntegerField(default = 0)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="quotes", on_delete = models.CASCADE, null = True)
    objects = Validator()