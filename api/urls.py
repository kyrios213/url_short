from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.home, name="home"),
    path('link_list/', views.ShortenerListAPIView.as_view(), name="list"),
    path('link_create/', views.ShortenerCreateAPIView.as_view(), name="create"),
]
