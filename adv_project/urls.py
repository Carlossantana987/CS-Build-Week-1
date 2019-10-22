# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls import include
# from rest_framework import routers
# from adventure.api import initialize, move, say
#
# router = routers.DefaultRouter()
# router.register(r'initialize', initialize)
# router.register(r'move', move)
# router.register(r'say', say)
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('api/adv/', include('adventure.urls')),
# ]






from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('login', obtain_auth_token, name='api_token_auth'),
]
