# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Docente(User):
	correo = models.CharField(u'Correo', max_length=15)
	cubiculo = models.CharField(u'Cubiculo', max_length=15)
	celular = models.CharField(u'Célular', max_length=15)

	def __unicode__(self):
		return self.first_name+' '+self.last_name
