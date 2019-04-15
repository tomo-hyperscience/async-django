from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('example2/', include('example2.urls')),
    path('example1/', include('example1.urls')),
    path('admin/', admin.site.urls),
]
