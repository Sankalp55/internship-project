from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Task
        fields = (
            'id',
            'owner',
            'title',
            'description',
            'status',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')

    def validate_status(self, value):
        """Ensure status is valid."""
        valid_statuses = ['pending', 'in-progress', 'completed']
        if value not in valid_statuses:
            raise serializers.ValidationError(
                f"Invalid status. Must be one of {valid_statuses}."
            )
        return value
