from django.urls import path
from . import views

app_name = 'picturalizer'

urlpatterns = [
    path('showall/', views.showall, name='showall'),
    path('upload/', views.upload, name='upload'),
    path('<int:image_id>/thread', views.thread, name='thread')
]
