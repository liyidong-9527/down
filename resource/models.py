from django.db import models
from user.models import User


# Create your models here.

class Resource(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, help_text="资源名")
    resource_type = models.CharField(max_length=10, help_text="资源类型")
    content_type = models.CharField(max_length=20, help_text="文件类型", blank=True)
    resource_key = models.CharField(max_length=50, help_text="关键字")
    resource_score = models.CharField(max_length=10, help_text="资源分")
    resource_text = models.CharField(max_length=200, help_text="资源描述")
    resource_user = models.CharField(max_length=20, help_text="上传者", blank=True)
    up_time = models.DateTimeField(auto_now=True)
    ext = models.CharField(max_length=10, help_text="文件后缀", blank=True)
    size = models.CharField(max_length=10, help_text="文件大小", blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="resource", null=True, blank=True)
    resource = models.FileField(upload_to="resource/resource_upload/", blank=True)
    download_num = models.CharField(max_length=20, help_text="下载次数", default=0)

    class Meta:
        
        db_table = "resource"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    com_user_id = models.CharField(max_length=10, help_text="评论用户id")
    com_time = models.DateTimeField(auto_now=True)
    com_text = models.CharField(max_length=200, help_text="评论内容")
    star = models.IntegerField(help_text="星级")
    resource = models.ForeignKey(to=Resource, on_delete=models.CASCADE, related_name="comment")

    class Meta:
        db_table = "comment"


class Collect(models.Model):
    coll_user = models.CharField(max_length=10, help_text="收藏用户id")
    coll_time = models.DateTimeField(auto_now=True)
    coll_resource = models.ForeignKey(to=Resource, on_delete=models.CASCADE, related_name="collect")

    class Meta:
        db_table = "collect"
