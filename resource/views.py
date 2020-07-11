from django.shortcuts import render, HttpResponse, redirect
from .forms import ResourceForm
from user.forms import UserInfoForm
from user.models import User
from .models import Resource, Comment, Collect
import json


# Create your views here.


def upload(request):
    form = ResourceForm(request.POST, request.FILES)
    if form.is_valid():
        form_data = form.instance
        form_file = form.files["resource"]
        print(dir(form_file))
        # 文件类型
        form_data.content_type = form_file.content_type
        # 上传用户
        form_data.resource_user = request.session["user"]["nickname"]
        # 后缀
        form_data.ext = form_file.name.split(".")[-1]
        # 文件大小
        form_data.size = form_file.size
        # 用户
        user_id = request.session["user"]["user"]
        form_data.user = User.objects.get(id=user_id)
        form_data.save()
    return redirect("/")


def comment(request):
    comment_dict = request.POST.dict()
    # 评论用户id
    com_user_id = request.session["user"]["user"]
    # 评论内容
    com_text = comment_dict["com_text"]
    # 星级
    star = comment_dict["star"]
    # id
    id = comment_dict["id"]
    resource = Resource.objects.get(id=id)
    # 数据保存到数据库
    com = Comment.objects.create(com_user_id=com_user_id, com_text=com_text, star=star, resource=resource)

    name = request.session["user"]["nickname"]

    comment_time = com.com_time.strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "comment_user": request.session["user"]["id"],
        "name": name,
        "time": comment_time,
        "star": star,
        "text": com_text,
    }
    data = json.dumps(data)
    return HttpResponse(data)


def collect(request):
    user_id = request.session["user"]["user"]
    resource_id = request.POST.dict()["resource_id"]
    if Collect.objects.filter(coll_user=user_id, coll_resource=Resource.objects.get(id=resource_id)):
        msg = {"status": 500}
    else:
        Collect.objects.create(coll_user=user_id, coll_resource=Resource.objects.get(id=resource_id))
        msg = {"statua": 200}
    msg = json.dumps(msg)
    return HttpResponse(msg)
