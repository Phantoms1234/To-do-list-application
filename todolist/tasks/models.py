from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.

class group(models.Model):

	Name=models.CharField(max_length=20)



	def __str__(self):
		return self.Name




	
class Task(models.Model):

	frequency_choices=[

	(timedelta(days=1) , "DAILY"),
	(timedelta(days=7) , "WEEKLY"),
	(timedelta(days=30) , "MONTHLY"),

	]

	#database model that contains all info relating to a task

	owner=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=50)
	date=models.DateTimeField()
	date_added=models.DateField(auto_now_add=True)
	description=models.TextField()
	frequency=models.DurationField(choices=frequency_choices,max_length=20,null=True,blank=True)
	duration=models.DurationField()
	due_date=models.DateField(null=True,blank=True)
	groups=models.ForeignKey(group,on_delete=models.CASCADE,null=True,blank=True)
	completed=models.BooleanField(default=False)


	


class Note(models.Model):
	#db model that keeps a note for jottings related to a task
	content=models.TextField()
	task=models.OneToOneField(Task,on_delete=models.CASCADE)
	


#could also add reminders (kinda like things i would like to remember on a particular day)











