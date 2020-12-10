from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from hrs.models import Employee, Hr
from rest_framework import serializers


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        data.update({'phone': self.user.phone})
        data.update({'first_name': self.user.first_name})
        data.update({'last_name': self.user.last_name})
        data.update({'is_superuser': self.user.is_superuser})
        return data


class EmployeeSerializer(serializers.ModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='employee-detail', format='html')
    class Meta:
        model = Employee
        fields ="__all__"

class HrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hr
        fields = ["phone","username","hr_image",]