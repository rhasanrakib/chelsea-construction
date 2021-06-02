from django.db import models
from django.utils import timezone

class Contact(models.Model):
    """Model definition for Contact."""
    created_time = models.DateTimeField('date created', default=timezone.now)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        ordering = ['-created_time']

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name

