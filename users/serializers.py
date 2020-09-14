from rest_framework import serializers
from users.models import User
from validate_docbr import CPF


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'password', 'cpf']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_cpf(self, value: str) -> str:
        cpf_validator = CPF()
        cpf = value

        if not cpf_validator.validate(cpf):
            raise serializers.ValidationError("Invalid CPF.")
        return cpf
