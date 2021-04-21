from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('accounts/', include('users.urls')),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')), 
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
