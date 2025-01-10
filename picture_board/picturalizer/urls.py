from django.urls import path
from . import views

app_name = 'picturalizer'

urlpatterns = [
    path('showall/', views.showall, name='showall'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('<int:pk>/thread', views.ThreadView.as_view(), name='thread')
]
