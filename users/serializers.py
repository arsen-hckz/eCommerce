from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True , min_length = 10)
    password2 = serializers.CharField(write_only = True )

    class Meta:
          model = User
          fields = ["id", "email", "username", "password", "password2", "phone", "address"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"error":"passwords dont match!"})
        
        return attrs

    def create(self,validated_data):
         validated_data.pop("password2")
         user = User.objects.create_user(**validated_data)
         return user

class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ["id", "email", "username", "phone", "address", "is_admin"]
          read_only_fields = ["id", "email", "is_admin"]