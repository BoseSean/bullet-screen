from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Color(models.Model):
    color_name =  models.TextField(max_length = 20, blank = False)
    color_value = models.TextField(max_length = 20, blank = False)

    def __unicode__(self):
        return self.color_name

class Bul(models.Model):
    bul_content = models.TextField(max_length = 100, blank = False)
    timestamp =  models.DateTimeField(auto_now=False, auto_now_add=True)
    bul_color = models.ForeignKey('Color', default=1)
    bul_size = models.IntegerField()
    if_shown = models.BooleanField(default=False)

    def __unicode__(self):
        return self.bul_content
    