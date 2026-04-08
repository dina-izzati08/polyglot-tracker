from django.db import models

class LearningEntry(models.Model):
    topic = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    minutes = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} ({self.language})"
 