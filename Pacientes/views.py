from django.shortcuts import render
from django.views.generic import CreateView,TemplateView, UpdateView, FormView,ListView,DetailView, DeleteView
from Pacientes.models import Seguimiento_Apoyo,Paciente,Historial_Medico,Defunciones
from django.core.urlresolvers import reverse_lazy
from Pacientes.forms import HistorialMedico_Form
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import Consulta_form

class Registro_paciente(CreateView):
	template_name='registro_paciente.html'
	model=Paciente
	fields='__all__'
	success_url=reverse_lazy('reporte_pacientes')

class Reporte_Paciente(ListView):
	template_name='reporte_pacientes.html'
	model=Paciente

# class Eliminar_Paciente(DeleteView):
#     model = Paciente
#     success_url = reverse_lazy('reporte_pacientes')

class EditarPaciente(PermissionRequiredMixin,UpdateView):
	permission_required='Pacientes.editar'
	model=Paciente
  	fields='__all__'
  	template_name='editar_paciente.html'
  	success_url=reverse_lazy('reporte_pacientes')

def Paciente_detalle(request,pk):
	p=Paciente.objects.get(id=pk)
	ph=Historial_Medico.objects.filter(Paciente_hm=pk)
	pa=Seguimiento_Apoyo.objects.filter(Apoyo_Paciente=pk)
	return render(request,'detalle_paciente.html',{'list':p,'list1':ph,'list2':pa}) 	
 	

class Registro_Historial(CreateView):
	template_name='registro_medico.html'
	model=Historial_Medico
	fields='__all__'
	success_url=reverse_lazy('reporte_pacientes')

#def Registro_Medico(request,pk):
	# form=HistorialMedico_Form(request.POST or None)
	# if request.method=='POST':
	# 	if form.is_valid():
	# 		p_paciente=pk
	# 		p_fecha=form.cleaned_data['Fecha']
	# 		p_diagnostico = form.cleaned_data['Diagnostico']

	# 		hm=Historial_Medico.objects.create(Paciente_hm=p_paciente,Fecha=p_fecha,Diagnostico=p_diagnostico)

	# 		return HttpResponseRedirect('/')
	# else:
	# 	form=HistorialMedico_Form()
	# ctx={'form':form}
	# return render(request,'registro_medico.html',ctx)

class Registro_Apoyo(CreateView):
	template_name='registro_apoyo.html'
	model=Seguimiento_Apoyo
	fields='__all__'
	success_url=reverse_lazy('reporte_apoyo')

class Reporte_Apoyo(ListView):
	template_name='reporte_apoyo.html'
	model=Seguimiento_Apoyo


class Registro_Defunciones(CreateView):
	template_name='registro_defunciones.html'
	model=Defunciones
	fields='__all__'
	success_url=reverse_lazy('ReporteDef_view')

class Reporte_Defunciones(ListView):
	template_name='reporte_defunciones.html'
	model=Defunciones

# class Eliminar_Defunciones(DeleteView):
#     model = Defunciones
#     success_url = reverse_lazy('reporte_defunciones')
def consulta (request):
	b = Paciente.objects.filter(Estado_salud='RE')
	c = Paciente.objects.filter(Estado_salud='TR')
	d = Paciente.objects.filter(Estado_salud='DEP')
	form = Consulta_form(request.POST or None)
	return render (request, 'consulta.html', {'list1' :b, 'list2' :c, 'list3' :d})