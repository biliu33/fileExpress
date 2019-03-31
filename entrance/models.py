# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    cTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["cTime"]