from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    يسمح بالقراءة للجميع (GET, HEAD, OPTIONS)
    ويمنع الكتابة إلا للمستخدمين المسؤولين (admins)
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

