from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView
from django.views import View
from django.conf import settings



from .models import Link
from .serializers import LinkSerializer

def home(request):
    return HttpResponse("Hello World")


class ShortenerListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ShortenerCreateAPIView(CreateAPIView):
    serializer_class = LinkSerializer


class Redirector(View):
    def get(self, request, shortener_link, *args, **kwargs):
        shortener_link = settings.HOST_URL + '/' + self.kwargs['shortener_link']
        redirect_link = Link.objects.filter(shortened_link=shortener_link).first().original_link
        return redirect(redirect_link)