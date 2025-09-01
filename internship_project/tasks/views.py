from rest_framework import generics, permissions, filters
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner
from django.utils import timezone
from datetime import timedelta
from rest_framework.response import Response
from rest_framework import status

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    queryset = Task.objects.all()

# Custom endpoint: completed tasks in last 7 days (owner-only)
from rest_framework.views import APIView
class RecentCompletedTasksView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        seven_days_ago = timezone.now() - timedelta(days=7)
        tasks = Task.objects.filter(owner=request.user, status='completed', updated_at__gte=seven_days_ago)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
