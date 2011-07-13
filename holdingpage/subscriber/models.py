from django.db import models

# Create your models here.
class Subscriber(models.Model):
    """
    A subscriber represents a visitor to the holding page who has left
    their details behind.
    """
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    share_code = models.CharField(max_length=10)
    source_share_code = models.CharField(max_length=10)