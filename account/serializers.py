from rest_framework import serializers
from .models import User




class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=200)
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )
    tc = serializers.BooleanField()

    def create(self,validated_Data):
         return User.objects.create_user(**validated_Data)


    def validate(self,attrs):
            password = attrs.get('password')
            password2 = attrs.get('password2')
            if password!= password2:
                raise serializers.ValidationError({
            'status': 'error',
            'code': 'PASSWORD_MISMATCH',
            'message': 'The passwords you entered do not match.',
            'suggestion': 'Please make sure both password fields contain the same value.'
        })
            return attrs
    




'''

class UserSerializer(serializers.Serializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['email','name','password','password2','tc']
        extra_kwargs = {
            'password':{'write_only':True}
        }

        def validate(self,attrs):
            password = attrs.get('password')
            password2 = attrs.get('password2')
            if password!= password2:
                raise serializers.ValidationError("password and confirm password doesnt match")
            return attrs
        
        def create(self,validate_data):
            return User.objects.Create(**validate_data) '''