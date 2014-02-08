# -*- coding: utf-8 -*-
from django.db import models


class OriginationPoint(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    login = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

    def login_password(self):
        return self.login + '@' + self.password
