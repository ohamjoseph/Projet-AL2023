from rest_framework import permissions

class PositionReadWritePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
    
class ColiReadWritePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True