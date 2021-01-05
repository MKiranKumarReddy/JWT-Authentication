from django.contrib import admin
from django.urls import path, include
from rest_auth.views import LogoutView
from api.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
admin.site.site_header = "HR Admin"
