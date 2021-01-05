from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework import viewsets
from api.models import Employee
from api.serializers import EmployeeSerializer, HRDashboardSerializer
from rest_framework import permissions

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class HRDashboardViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = HRDashboardSerializer


class CustomLoginView(ObtainJSONWebToken):

    def post(self, request, *args, **kwargs):

        username = request.data.get('username', None)
        password = request.data.get('password', None)

        error_message = {}
        if not username:
            error_message['username'] = ["This field is required"]
        if not password:
            error_message['password'] = ["This field is required"]
        if len(error_message) > 0:
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)

