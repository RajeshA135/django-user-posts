from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()   
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email','age','address']
        extra_kwargs={'password':{'write_only':True}}
    def create(self, validated_data):
        user=User.objects.create_user(
        username=validated_data['username'],
        password=validated_data['password'],
        email=validated_data['email'],
        age=validated_data['age'],
        address=validated_data['address']
        )
        return user