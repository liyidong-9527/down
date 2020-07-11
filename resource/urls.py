from django.urls import path
from . import views

urlpatterns = [
    path("upload", views.upload),
    path("comment", views.comment),
    path("collect", views.collect),

]