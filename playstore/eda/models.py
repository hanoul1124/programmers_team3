from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        )
    image = models.ImageField(
        blank=True,
        null=True
        )
    description = models.TextField(
        blank=True,
        null=True,
        )
    