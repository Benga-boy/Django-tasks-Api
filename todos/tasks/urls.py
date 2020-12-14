from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.tasksList, name="task-list"),
    path('task-detail/<str:pk>/', views.detailView, name="detail-view"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('task-update/<str:pk>', views.updateTask, name="task-update"),
    path('task-create/', views.createTask, name="task-create")
]