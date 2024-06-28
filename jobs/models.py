from django.db import models

# Create your models here.

class Jobs(models.Model):
    company = models.CharField(max_length=100)
    logo =models.ImageField(upload_to='images/',default='images/default.jpg')
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    deadline = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.title