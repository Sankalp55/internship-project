from rest_framework import generics, permissions, filters, status
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

    def get_queryset(self):
        # Only show tasks owned by the logged-in user
        return Task.objects.filter(owner=self.request.user)

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
        seven_days_ago = timezone.now() - timedelta(days=7)
        tasks = Task.objects.filter(
            owner=request.user,
            status='completed',
            updated_at__gte=seven_days_ago
        )
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
