
# from django.urls import path, include
# from rest_framework import routers
from django.urls import re_path
from . import views

# router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)

urlpatterns = [
    re_path(r'^hero$', views.heroApi),
    re_path(r'^hero/([0-9]+)$', views.heroApi)
]