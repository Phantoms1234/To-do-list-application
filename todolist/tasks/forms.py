from django import forms 
from .models import Task, Note



class task_form(forms.ModelForm):

	date=forms.DateTimeField(widget=forms.SelectDateWidget())
	due_date=forms.DateTimeField(widget=forms.SelectDateWidget())
	#duration=forms.DurationField(widget=forms.DurationInputWidget())


	class Meta:

		model=Task
		fields=['title','date','description','duration','due_date','frequency']



		
		

