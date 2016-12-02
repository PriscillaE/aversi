from django.shortcuts import render
from django.views.generic import CreateView,TemplateView, UpdateView, FormView,ListView,DetailView, DeleteView
from .models import Personal,Administradores,Minutas,Eventos
from django.core.urlresolvers import reverse_lazy
from Pacientes.forms import HistorialMedico_Form
from django.contrib.auth.mixins import PermissionRequiredMixin

class Index_view(TemplateView):
	template_name = 'index.html'

class Mision_view(TemplateView):
	template_name = 'mision.html'

class Historia_view(TemplateView):
	template_name = 'historia.html'

class Ubicacion_view(TemplateView):
	template_name = 'ubicacion.html'

# Create your views here.
class Registro_Minutas(CreateView):
	template_name='registro_minutas.html'
	model=Minutas
	fields='__all__'
	success_url=reverse_lazy('reporte_minutas')

class Detalle_minuta(DetailView):
	template_name='detalle_minuta.html'
	model=Minutas

class Reporte_Minutas(ListView):
	template_name='reporte_minutas.html'
	model=Minutas

class Editar_Minuta(UpdateView):
  	model=Minutas
  	fields='__all__'
  	template_name='editar_minuta.html'
  	success_url=reverse_lazy('ReporteMin_view')

class Registro_Eventos(CreateView):
	template_name='registro_eventos.html'
	model=Eventos
	fields='__all__'
	success_url=reverse_lazy('reporte_eventos')

class Eliminar_Eventos(DeleteView):
    model = Eventos
    success_url = reverse_lazy('reporte_eventos')

class Editar_Evento(UpdateView):
  	model=Eventos
  	fields='__all__'
  	template_name='editar_evento.html'
  	success_url=reverse_lazy('ReporteEve_view')

class Reporte_Eventos(ListView):
	template_name='reporte_eventos.html'
	model=Eventos

class Detalle_eventos(DetailView):
	template_name='detalle_evento.html'
	model=Eventos

class Registro_Personal(CreateView):
	template_name='registro_personal.html'
	model=Personal
	fields='__all__'
	success_url=reverse_lazy('reporte_personal')

#class Eliminar_Personal(DeleteView):
#   model = Personal
#    success_url = reverse_lazy('reporte_personal')

class Editar_Personal(UpdateView):
  	model=Personal
  	fields='__all__'
  	template_name='editar_personal.html'
  	success_url=reverse_lazy('reporte_personal')

class Reporte_Personal(ListView):
	template_name='reporte_personal.html'
	model=Personal


class CrearUsAdmon(PermissionRequiredMixin,CreateView):
	permission_required='crear_admin'
	template_name='crear_admon.html'
	model=Administradores
	fields='__all__'
	success_url=reverse_lazy('login')

class Donar(TemplateView):
	template_name='donaciones.html'

class Galeria(TemplateView):
	template_name='galeria.html'

