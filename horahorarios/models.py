from __future__ import unicode_literals
from docentes.models import Docentes
from django.db import models

class Materias(models.Model):
	nombre = models.CharField(u'Materia',max_length=100)
	carrera = models.CharField(u'Carrera',max_length=100)
	def __unicode__(self):
		return self.nombre

class Horario(models.Model):
	diaSemana = models.CharField(u'Correo', max_length=15)
	aula = models.CharField(u'Cubiculo', max_length=15)
	docente = models.ForeignKey(u'Docente', Docentes)
	grupo =
	materia = models.ForeignKey(u'Docente', Docentes)

	def __unicode__(self):
		return self.first_name+' '+self.last_name

