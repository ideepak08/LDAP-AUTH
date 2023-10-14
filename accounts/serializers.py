from rest_framework import serializers
from .models import CustomUser


class LDAPAuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    # role = serializers.ChoiceField(choices=CustomUser.ROLE_CHOICES)
