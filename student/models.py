from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Registered at')

    def __str__(self):
        return self.name
