from django.shortcuts import render
from django.http import HttpResponse
from myproject.models import Alunos

from django.views.generic import ListView
from django.views.generic.edit import UpdateView

# Create your views here.

def home(request):
	#return HttpResponse('Index do Gestor de bases')
	alunos = Alunos.alunos.all()
	contexto = {'alunos': alunos}
	return render(request, 'bases/index.html', contexto)


def dashboard(request):
	return render(request, 'bases/dashboard.html', {})



def cadastroBase(request):
	return render(request, 'bases/cadastroBase.html', {})


class AlunosListView(ListView):
	template_name = 'bases/index.html'
	model = Alunos
	context_object_name = 'alunos'




class AlunosUpdateView(UpdateView):
	template_name = 'bases/editaAluno.html'
	model = Alunos
	fields = ['seq_geral', 'matricula', 'nome', 'nome_mae'] # Lista de campos disponibilizados para edição
	context_object_name = 'aluno'

	def get_object(self, queryset=None):
		aluno = None
		id = self.kwargs.get(self.pk_url_kwarg)
		slug = self.kwargs.get(self.slug_url_kwarg)
		if id is not None:
			# Busca o aluno apartir do id
			aluno = Alunos.alunos.filter(seq_geral=id).first()
		elif slug is not None:
			# Pega o campo slug do Model
			campo_slug = self.get_slug_field()
			# Busca o aluno apartir do slug
			aluno = Alunos.alunos.filter(**{campo_slug: slug}).first()
		# Retorna o objeto encontrado
		return aluno