from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Link
from .serializers import LinkSerializer

def home(request):
    return HttpResponse("Hello World")


class ShortenerListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ShortenerCreateAPIView(CreateAPIView):
    serializer_class = LinkSerializer