from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import RegisterSerializer, UserSerializer
from users.tasks import send_welcome_email

def home(request):
    return render(request, "index.html")


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
       
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()

       
        send_welcome_email.delay(user.email)

        return Response(
            {
                "message": "User registered successfully!",
                "user": UserSerializer(user).data
            },
            status=status.HTTP_201_CREATED
        )


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        """Allow user to update only profile fields (like full_name)."""
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

       
        data = request.data.copy()
        data.pop("email", None)

        serializer = self.get_serializer(instance, data=data, partial=partial)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)
