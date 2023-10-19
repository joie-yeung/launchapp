import datetime

from django.db import models
from django.utils import timezone

# project name, project description, project due date, team members
class Project(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField("due date")
    # new_field = models.CharField(max_length=140, default='SOME STRING')
    description = models.TextField(max_length=500, default="")
    proj_id = models.IntegerField()
    # store team members in a array
    def __str__(self):
        return self.name
    def due_soon(self):
        return self.date >= timezone.now() - datetime.timedelta(days=7)


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text
    
