from django import forms

class InsereAlunosForm(forms.ModelForm):
	
	class Meta:
		model = Alunos

		fields = ['matricula', 'nome', 'nome_mae']