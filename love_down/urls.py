"""love_down URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .import views
urlpatterns = [
    # path("/", views.index),
    # path("index", views.index),
    path("bbs", views.bbs),
    path("bbsdetail", views.bbsdetail),
    path("index", views.index),
    path("upload", views.upload),
    path("personal", views.personal),
    path("shoucang", views.shoucang),
    path("point", views.point),
    path("detail/<int:id>", views.detail),
    path("logout", views.logout),
    url("^$", views.index),
    url("^resource/", include("resource.urls")),
    url("^user/", include("user.urls")),
]
