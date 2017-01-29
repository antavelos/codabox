from django.db import models


class Entity(models.Model):
    class Meta:
        verbose_name_plural = "entities"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
