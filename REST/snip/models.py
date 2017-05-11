from django.db import models

# Create your models here.
class Snip(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=200, default='Python')
    style = models.CharField(max_length=200, default='friendly')

    class Meta:
        ordering = ('created',)