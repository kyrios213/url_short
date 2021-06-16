from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.ShortenerListAPIView.as_view(), name="list"),
    path('create/', views.ShortenerCreateAPIView.as_view(), name="create"),
]
