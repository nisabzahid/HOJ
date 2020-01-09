from django.contrib import admin
from .models import Problem
# Only admin can add/edit problem
admin.site.register(Problem)
