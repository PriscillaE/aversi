from django.shortcuts import render
from django.views.generic import CreateView,TemplateView, UpdateView, FormView,ListView,DetailView, DeleteView
from .models import Donadores,Donaciones_Monetarias, Donaciones_Especie
from Pacientes.models import Seguimiento_Apoyo,Defunciones
from django.core.urlresolvers import reverse_lazy
from Pacientes.forms import HistorialMedico_Form
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Sum
from django.shortcuts import render_to_response
from datetime import datetime, time, date, timedelta
from django.http import HttpResponseRedirect,HttpResponse
from django.core import serializers



class Register_Donadores(CreateView):
	template_name ='registro_donadores.html'
	model = Donadores
	fields = '__all__'
	success_url = reverse_lazy('Register_Donadores')
class Register_Donaciones_Monetarias(CreateView):
	template_name ='registro_donadores_monetarias.html'
	model = Donaciones_Monetarias
	fields = '__all__'
	success_url = reverse_lazy('Donadores_monetarias_register_view')
class Register_Donaciones_Especie(CreateView):
	template_name ='registro_donadores_especie.html'
	model = Donaciones_Especie
	fields = '__all__'
	success_url = reverse_lazy('Donadores_especie_register_view')
class donadores_report(ListView):
	template_name = 'donadores_report.html'
	model = Donadores
class donaciones_monetarias_report(ListView):
	template_name = 'donaciones_monetarias_report.html'
	model = Donaciones_Monetarias
class donaciones_especie_report(ListView):
	template_name = 'donaciones_especie_report.html'
	model = Donaciones_Especie
class Editar_Donador(PermissionRequiredMixin,UpdateView):
	permission_required='Pacientes.editar'
  	model=Donadores
  	fields='__all__'
  	template_name='eliminar_donadores.html'
  	success_url=reverse_lazy('Donadores_eliminar_view')

class EditarDonaciones_monetarias(PermissionRequiredMixin, UpdateView):
	permission_required='Pacientes.editar'
  	model=Donaciones_Monetarias
  	fields='__all__'
  	template_name='eliminar_donaciones_monetarias.html'
  	success_url=reverse_lazy('Donaciones_monetarias_eliminar_view')

class Editar_Donaciones_especie(PermissionRequiredMixin, UpdateView):
	permission_required='Pacientes.editar'
  	model=Donaciones_Especie
  	fields='__all__'
  	template_name='eliminar_donaciones_especie.html'
  	success_url=reverse_lazy('Donadores_especie_eliminar_view')

def wsUltimoDonaciones(request):
	actual=datetime.now()
	data=serializers.serialize('json',Donaciones_Monetarias.objects.filter(Fecha__month=actual.month).select_related('Donador'))
	#print data
	return HttpResponse(data,content_type='application/json')

def wsUltimoDefunciones(request):
	actual=datetime.now()
	data=serializers.serialize('json',Defunciones.objects.filter(Fecha_apoyo__month=actual.month).select_related('Paciente'))
	#print data
	return HttpResponse(data,content_type='application/json')

def wsUltimoApoyo(request):
	actual=datetime.now()
	data=serializers.serialize('json',Seguimiento_Apoyo.objects.filter(Fecha_entrega__month=actual.month).select_related('Apoyo_Paciente'))
	#print data
	return HttpResponse(data,content_type='application/json')

class ReporteMensual(TemplateView):
	template_name='reporte_mensual.html'