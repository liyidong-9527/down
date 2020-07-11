from django.forms import models
from .models import User, User_info


class UserForm(models.ModelForm):
    # 和模型进行绑定
    class Meta:
        model = User
        fields = ["username", "password"]
        # fields = "__all__"


class UserInfoForm(models.ModelForm):
    class Meta:
        model = User_info
        fields = "__all__"
