from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission:
    - Owners can view/edit/delete
    - Others can only view (safe methods)
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return obj.owner == request.user
