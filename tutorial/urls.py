from django.contrib import admin
from django.urls import path, include
from .quickstart.urls import router as quickstart_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(quickstart_router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework'))
]
