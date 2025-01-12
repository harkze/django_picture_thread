from django.urls import path
from . import views

app_name = 'picturalizer'

urlpatterns = [
    path('showall/', views.ShowAllView.as_view(), name='showall'),
    path('upload/', views.ImageUploadView.as_view(), name='imageupload'),
    path('<int:pk>/thread', views.thread, name='thread'),
]
