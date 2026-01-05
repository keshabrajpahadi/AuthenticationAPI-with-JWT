from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer,UserLoginSerializer
from django.contrib.auth import authenticate
from .renderers import UserRenderer
# Create your views here.

class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request):
            serilaizer=UserLoginSerializer(data=request.data)
            if serilaizer.is_valid(raise_exception=True):
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
    
class UserlLoginView(APIView):
    def post(self,request):
            serilaizer=UserLoginSerializer(data=request.data)
            if serilaizer.is_valid(raise_exception=True):
                email=serilaizer.data.get('email')
                password=serilaizer.data.get('password')
                user= authenticate(email=email,password=password)
                if user is not None:
                    messages = {
                    "response_code":"1",
                    "response":"successfull",
                      }
                    return Response(messages,status=status.HTTP_201_CREATED)
            
                else:
                 messages = {
                                "response_code":"0",
                                "response":"unsucces ",
                                'non_field_errors': ['email or password is not valid']
                            }
                 return Response(messages,status=status.HTTP_400_BAD_REQUEST)
            messages = {
                                "response_code":"0",
                                "response":"unsucces ",
                                'errors': serilaizer.errors
                            }
            return Response(messages,status=status.HTTP_400_BAD_REQUEST)
    
                    


