""" Views
"""
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """An endpoint that allows users to be viewed or edited

    Args:
        viewsets (_type_): _description_
    """
    queryset = User.objects.all().order_by('-date-joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """An endpoint that allows groups to be viewed or edited

    Args:
        viewsets (_type_): _description_
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
