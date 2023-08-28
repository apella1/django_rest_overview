""" Serializers
"""
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User serializer

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        """_summary_
        """
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """ Group serializer

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        """_summary_
        """
        model = Group
        fields = ['url', 'name']
