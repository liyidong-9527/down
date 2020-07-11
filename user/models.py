from django.db import models


# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, help_text="账户")
    password = models.CharField(max_length=50, help_text="密码")

    class Meta:
        db_table = "user"


class User_info(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=20, help_text="昵称")
    realname = models.CharField(max_length=20, help_text="真实姓名")
    user_email = models.EmailField(help_text="邮箱")
    user_phone = models.CharField(max_length=20, help_text="联系方式")
    sex = models.CharField(max_length=1, help_text="性别")
    photo = models.BinaryField()
    reg_time = models.DateTimeField(auto_now=True)
    user_score = models.CharField(max_length=100, help_text="积分", default=20)
    # 设置外键关联
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="info")

    class Meta:
        db_table = "user_info"
