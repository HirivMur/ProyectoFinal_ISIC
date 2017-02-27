from django.shortcuts import render
from models import Docente

def docentesproy(request):
	return render(request,'base.html')

def listaDocentes(request):

	docentes = Docente.objects.all()
	return render(request, 'listaDocentes.html', {'docentes':docentes})
