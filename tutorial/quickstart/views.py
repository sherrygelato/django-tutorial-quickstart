from django.contrib.auth.models import User, Group
from rest_framework import viewsets 
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

# viewsets : 모든 일반적인 동작을 클래스로 그룹화하여 간결화

class UserViewSet(viewsets.ModelViewSet):
    """
    사용자를 보거나 편집할 수 있는 API endpoint
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    사용자를 보거나 편집할 수 있는 API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]