from django.db import models


class Colors(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)
