"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.tracking import views as tracking_views

tracking_router = routers.DefaultRouter()
tracking_router.register(r'users', tracking_views.UserViewSet)
tracking_router.register(r'groups', tracking_views.GroupViewSet)
tracking_router.register(r'set', tracking_views.SetViewSet)
tracking_router.register(r'workout', tracking_views.WorkoutViewSet)
tracking_router.register(r'exercise', tracking_views.ExerciseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(tracking_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
