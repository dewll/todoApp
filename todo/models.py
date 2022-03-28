from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    '''
    This is a Todo model that represent the column table in the database
    '''
    title = models.CharField(max_length = 50)
    description = models.TextField()
    date = models.DateField(default = timezone.now().strftime("%Y-%m-%d"))
    completed = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.title} {self.description} {self.completed}"