from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .models import Autoevaluaciones
from .forms import AutoevaluacionForm

# Create your views here.
class Crear(LoginRequiredMixin, CreateView): #SIEMPRE EL LOGIN SE HEREDA PRIMERO
	model = Autoevaluaciones
	form_class = AutoevaluacionForm
	template_name = 'autoevaluacion/test.html'
	success_url = reverse_lazy('home')#Modificar luego para saber el resultado del test

class Listar(ListView):
	model = Autoevaluaciones
	template_name = 'autoevaluacion/listado.html'

def CrearEvaluacion(request):
	if request.method == 'POST':
		form = AutoevaluacionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/', pk=post.clave)
	else:
		form = AutoevaluacionForm()

	return render(request, 'autoevaluacion/testFuncion.html',{'form': form})
