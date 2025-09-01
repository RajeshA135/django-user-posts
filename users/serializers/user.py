from rest_framework import serializers
from ..models import CustomUser

# User Serializer (for registration and profile)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "age", "address", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
            age=validated_data.get("age"),
            address=validated_data.get("address"),
        )
        return user

