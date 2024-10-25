
from django.urls import path,include
from .views import api_list,api_detailview

urlpatterns = [
    path("",api_list.as_view(),name="api_tasklist_view"),
    path("<int:pk>",api_detailview.as_view(),name="api_taskdetail_view"),

]



