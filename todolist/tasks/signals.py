from django.dispatch import receiver
from .models import Task
from django.db.models.signals import post_save
from datetime import date,timedelta

@receiver(post_save,sender=Task)
def duplicate_task_thread(sender,created,instance,**kwargs):
	if created and instance.frequency:
		days=(instance.due_date-instance.date.date()).days


		#if tasks is a daily task
		if instance.frequency==timedelta(days=1):
			n=1
			for num in range(days):
				Task.objects.create(
					owner=instance.owner,
					title=instance.title,
					description=instance.description,
					duration=instance.duration,
					date_added=instance.date_added,
					date=instance.date+(n*instance.frequency)

					)
				n=n+1


		#if task is weekly
		elif instance.frequency==timedelta(days=7):
			n=1
			weeks=days//7
			for num in range(weeks):
				Task.objects.create(
					owner=instance.owner,
					title=instance.title,
					description=instance.description,
					duration=instance.duration,
					date_added=instance.date_added,
					date=instance.date+(n*instance.frequency)

					)
				n=n+1

		#if task is monthly
		else:
			n=1
			months=days//30
			for num in range(months):
				Task.objects.create(
					owner=instance.owner,
					title=instance.title,
					description=instance.description,
					duration=instance.duration,
					date_added=instance.date_added,
					date=instance.date+(n*instance.frequency)

					)
				n=n+1







