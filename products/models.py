# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length = 200)
	description = models.CharField(max_length = 1000)

	def __str__(self):
		return self.name