from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created  = models.DateTimeField(auto_now_add=True)
    title    = models.CharField(max_length=100, blank=True, default='')
    code     = models.TextField()
    linenos  = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='Python', max_length=100)
    style    = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created', )

# 用户模型
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    idcard   = models.CharField(max_length=20)
    is_vip   = models.BooleanField(default=False)
    car_type = models.CharField(max_length=200)