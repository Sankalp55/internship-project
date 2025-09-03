from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner


# -------------------------------
# List + Create Tasks
# -------------------------------
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'status']
    ordering_fields = ['created_at', 'updated_at', 'status']

    def get_queryset(self):
        """
        Return only tasks owned by the logged-in user.
        Support optional filtering by status.
        Example: /api/tasks/?status=completed
        """
        user = self.request.user
        queryset = Task.objects.filter(owner=user)

        status_param = self.request.query_params.get("status")
        if status_param:
            queryset = queryset.filter(status=status_param)

        return queryset

    def perform_create(self, serializer):
        # Assign owner automatically on creation
        serializer.save(owner=self.request.user)


# -------------------------------
# Retrieve + Update + Delete a Task
# -------------------------------
class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    queryset = Task.objects.all()


# -------------------------------
# Custom: Completed Tasks in Last 7 Days
# -------------------------------
class RecentCompletedTasksView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        """
        Get all completed tasks in the last 7 days for the logged-in user.
        """
        seven_days_ago = timezone.now() - timedelta(days=7)
        tasks = Task.objects.filter(
            owner=request.user,
            status='completed',
            updated_at__gte=seven_days_ago
        )
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
