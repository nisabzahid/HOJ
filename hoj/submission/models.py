from django.db import models
from user.models import UserSignup
from problems.models import Problem

#user submitted code save to "media/user <id>/filename"
def path_to_save(instance, filename):
    return 'user {0}/{1}'.format(instance.user_id.id, filename)

LANG_CHOICES = (
        ('C', 'C'),
        ('C++', 'C++'),
        ('Python', 'Python'),
)
VERDICT_CHOICES =   (
        (0, 'Pending'),
        (1, 'Accepted'),
        (2, 'Wrong Answer'),
        (3, 'Compilation Error'),
        (4, 'Time Limit Exceeded'),
        (5, 'Memory Limit Exceeded'),
        (6, 'Run Time Error'),
)
class Submission(models.Model):
    user_id = models.ForeignKey(UserSignup, on_delete = models.CASCADE)
    problem_id = models.ForeignKey(Problem, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length = 10, choices = LANG_CHOICES, default = 'C++')
    verdict = models.IntegerField(choices = VERDICT_CHOICES, default = 0)
    time = models.DecimalField(max_digits=5, decimal_places=3, default = 0.0)
    memory = models.IntegerField(default = 0)
    code = models.FileField(upload_to = path_to_save)

    def __str__(self):
        return str(self.id)
    
