from __future__ import unicode_literals
from django.db import models
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 10:
            errors["name"] = "Course name should be more than 10 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Course description should be more than 15 characters"
        return errors;
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
