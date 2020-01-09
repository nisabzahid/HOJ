from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

#def path_to_save(instance, filename):
#    return 'user {0}/{1}'.format(instance.user_id.id, filename)

class UserSignup(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    problem_tried = models.IntegerField(default = 0)
    problem_solved = models.IntegerField(default = 0)

    def __str__(self):
        return self.username
'''
#this is should be the main model, userSignup fields need to add in it
class Profile(models.Model):
    user_id = models.ForeignKey(UserSignUp, on_delete = models.CASCADE)
    institute = Models.CharField(max_length = 100)
    photo = Models.ImageField(upload_to = path_to_save, default = 'media/default_img.jpg')
    problem_solved = ArrayField(models.CharField())
    problem_unsolved = ArrayField(models.CharField())
'''
