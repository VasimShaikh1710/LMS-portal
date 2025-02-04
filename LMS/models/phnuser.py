from django.db import models

class Phnuser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
