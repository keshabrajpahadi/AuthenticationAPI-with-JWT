from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

# Create your views here.

class UserRegistrationView(APIView):
    def post(self,request):
            serilaizer=UserSerializer(data=request.data)
            if serilaizer.is_valid():
                  user=serilaizer.save()
                  messages = {
                    "response_code":"1",
                    "response":"successfull",
                    "data":serilaizer.data
                      }
                  return Response(messages,status=status.HTTP_201_CREATED)

            messages = {
                "response_code":"0",
                "response":"unsucces ",
                "error":serilaizer.errors
            }
            return Response(messages,status=status.HTTP_400_BAD_REQUEST)
