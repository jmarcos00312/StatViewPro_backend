
from django.contrib import admin
from django.urls import path, include
from nbadle.api import get_76ers_players, get_all_players




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/76ers/players/', get_76ers_players, name='76ers-players'),
    path('api/players/', get_all_players, name='players-api'),
    # Add the following URL pattern for the root path
    # path('', redirect_to_homepage),  # Replace `redirect_to_homepage` with your view or redirect
]