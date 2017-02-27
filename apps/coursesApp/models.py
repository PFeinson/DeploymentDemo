from __future__ import unicode_literals

from django.db import models

from ..loginAndReg.models import User
# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length=75, default='')
    course_description = models.CharField(max_length=200, default = '')
    created_at = models.DateTimeField(auto_now_add=True)
    all_users = models.ManyToManyField(User, related_name = "all_users")
    #def create(cls, name, descr):
    #    course = cls(course_name = name, course_description = descr, created_at = datetime.datetime.now())
    #    return course
