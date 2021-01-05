
from rest_framework import routers
from django.urls import path, include
from api.views import EmployeeViewSet, HRDashboardViewSet

router = routers.DefaultRouter()
router.register(r'hrdashboard', HRDashboardViewSet)
router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('v1/',include(router.urls)),


]
