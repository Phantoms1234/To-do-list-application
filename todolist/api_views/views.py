from rest_framework import generics
from tasks.models import Task
from .serializers import TaskSerializer




class api_list(generics.ListCreateAPIView):
	queryset=Task.objects.all()
	serializer_class= TaskSerializer





	def perform_create(self, TaskSerializer):
		TaskSerializer.save(owner=self.request.user)




class api_detailview(generics.RetrieveUpdateDestroyAPIView):
	queryset=Task.objects.all()
	serializer_class= TaskSerializer
