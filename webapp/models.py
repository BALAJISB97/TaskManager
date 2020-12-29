from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    TaskName = models.CharField(max_length=40)
    TaskDescription = models.TextField()
    isCompleted = models.BooleanField(default=False)
    TaskAddedTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.TaskName