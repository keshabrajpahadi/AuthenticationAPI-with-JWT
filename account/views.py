from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer,UserLoginSerializer,UserProfileSerializer
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
# Create your views here.
#generate token manually 
def get_tokens_for_user(user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request):
            serilaizer=UserLoginSerializer(data=request.data)
            if serilaizer.is_valid(raise_exception=True):
                  user=serilaizer.save()
                  token=get_tokens_for_user(user)
                  messages = {
                    "response_code":"1",
                    "response":"successfull",
                    'token':token,
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
                    token = get_tokens_for_user(user)
                    messages = {
                    "response_code":"1",
                    "response":"successfull",
                    'token':token
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
    


class UserProfileView(APIView):
     renderer_classes=[UserRenderer]
     permission_classes = [IsAuthenticated]
     def get(self,request,format=None):
          serilaizer=UserProfileSerializer(request.user) 
          if serilaizer.is_valid():
               messages = {
                    'response':1,
                    "response":"dispaly data ",
                    "data":serilaizer.data
               }
               return Response(messages,status=status.HTTP_200_OK)
    
                    


