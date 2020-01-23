# Django imports
from django.shortcuts import render

# Django REST framework imports
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

# App imports
from .serializers import PlanSerializer, RegisterSerializer

class PlanView(APIView):
    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer