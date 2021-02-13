from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(max_length=1000)
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
