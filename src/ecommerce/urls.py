from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from drf_spectacular.views import SpectacularAPIView, \
    SpectacularRedocView, SpectacularSwaggerView


apiurlpatterns = [
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),

]

urlpatterns = [
    path('api/v1/', include(apiurlpatterns)),
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
