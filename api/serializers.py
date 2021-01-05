from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super(EmployeeSerializer, self).to_representation(instance)
        if rep['hr']:
            rep['hr'] = str(instance.hr)

        return rep

    class Meta:
        model = Employee
        fields = '__all__'


class HRDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'