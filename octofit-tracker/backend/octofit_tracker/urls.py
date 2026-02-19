"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os


@api_view(['GET'])
def api_root(request, format=None):
    """
    API root endpoint that lists all available endpoints.
    Constructs URLs using CODESPACE_NAME environment variable for Codespaces.
    """
    codespace_name = os.environ.get('CODESPACE_NAME')
    
    # Determine the base URL based on the request or environment
    if codespace_name:
        base_url = f'https://{codespace_name}-8000.app.github.dev'
    else:
        # Use the request to build the URL for localhost
        scheme = request.scheme
        host = request.get_host()
        base_url = f'{scheme}://{host}'
    
    return Response({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'leaderboard': f'{base_url}/api/leaderboard/',
        'workouts': f'{base_url}/api/workouts/',
    })


urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]

