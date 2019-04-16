from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('connection', views.connection, name='connection'),
    path('file', views.file, name='file')
]
