from rest_framework import serializers
from tasks.models import Task,group


class TaskSerializer(serializers.ModelSerializer):
	#groups=serializers.PrimaryKeyRelatedField(queryset=group.objects.all())


	class Meta:
		model = Task
		fields = (
			"title",
			"description",
			"frequency",
			"duration",
			"due_date",
			"completed",
			"groups",
			"date"

			)
