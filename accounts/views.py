from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LDAPAuthenticationSerializer


class LDAPAuthenticationView(APIView):
    def post(self, request):
        serializer = LDAPAuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Generate a new access token
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response(
                    {"access_token": access_token, "message": "Login successful"}
                )
            else:
                return Response(
                    {"message": "Login failed"}, status=status.HTTP_401_UNAUTHORIZED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
