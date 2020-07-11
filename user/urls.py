from django.urls import path
from . import views

urlpatterns = [
    path("reg", views.reg),
    path("reg2", views.reg2),
    path("reg3", views.reg3),
    path("check_user", views.check_user),
    path("login", views.login),
    path("user/<int:id>", views.show_photo),
    path("modifypass", views.modifypass),
    path("check_pwd", views.check_pwd),
    path("change_pwd", views.change_pwd),
]