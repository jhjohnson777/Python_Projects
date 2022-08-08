from django.db import models

PREFIX_CHOICES = (
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Ms','Ms'),
)
class Profile(models.Model):
    Prefix = models.CharField(max_length=5,choices=PREFIX_CHOICES)
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    Email = models.CharField(max_length=60)
    Username = models.CharField(max_length=60)

    objects = models.Manager()

    def __str__(self):
        return self.FirstName
