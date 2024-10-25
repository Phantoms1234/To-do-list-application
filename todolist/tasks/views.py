from django.shortcuts import render,redirect
from .models import Task
from .forms import task_form
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):

	return render(request, "tasks/task_view.html", {"tasks":Task.objects.all()})


@login_required
def createtask(request):

	if request.method=="POST":
		form=task_form(request.POST)
		if form.is_valid():
			filledform=form.save(commit=False)
			filledform.owner=request.user
			filledform.save()
			return redirect("task_view")



	form=task_form()



	return render(request, "tasks/create_task.html",{"form":form})











	



# task view should be here 



#i could also create a list view of all my tasks here
# would be advantageous to use a list view kinda so i can double it into a weekly or day view 




