from django.shortcuts import render

from .models import *

from .serializers import *

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status

class Currencies(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrenciesSerializer
    permission_classes = [IsAuthenticated]

class Currency(generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrenciesSerializer
    permission_classes = [IsAuthenticated]


class Register(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class Login(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)