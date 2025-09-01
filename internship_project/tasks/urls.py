from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, RecentCompletedTasksView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='tasks-list-create'),
    path('<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('recent-completed/', RecentCompletedTasksView.as_view(), name='recent-completed'),
]
