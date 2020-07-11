from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from user.models import User
from resource.models import Resource, Comment, Collect
import json

def index(request):
    resource = Resource.objects.all()
    all_resource = []
    one_resource = {}
    for r in resource:
        # 资源名称
        one_resource["name"] = r.name
        # 后缀
        one_resource["ext"] = r.ext
        # 上传者
        one_resource["user"] = r.resource_user
        # 上传时间
        one_resource["up_time"] = r.up_time.strftime("%Y-%m-%d %H:%M")
        # 积分
        one_resource["score"] = r.resource_score
        # 资源id
        one_resource["id"] = r.id
        all_resource.append(one_resource)
        one_resource = {}
    u = request.session.get("user")
    if not u:
        return render(request, "index.html", {"resource": all_resource})
    else:
        info = request.session["user"]
        u_id = info["id"]
        return render(request, "index.html", {"id": u_id, "resource": all_resource})


def logout(request):
    request.session.flush()
    return redirect("/")


def bbs(request):
    return render(request, "bbs.html")


def bbsdetail(request):
    return render(request, "bbsdetail.html")


def upload(request):
    return render(request, "upload.html")


# 个人信息页
def personal(request):
    user = request.session.get("user")
    return render(request, "personal.html", {"user": user})

# 收藏页
def shoucang(request):
    user_id = request.session["user"]["user"]
    collect = Collect.objects.filter(coll_user=user_id)
    msg = []
    msg_ = {}
    for i in collect:
        resource_id = i.coll_resource_id
        res = Resource.objects.get(id=resource_id)
        msg_ = {
            "name": res.name,
            "ext": res.ext,
            "user": res.resource_user,
            "time": i.coll_time.strftime("%Y-%m-%d %H:%M:%S"),
            "score": res.resource_score
        }
        msg.append(msg_)
    return render(request, "shoucang.html", {"msg": msg})


def point(request):
    return render(request, "point.html")


# 详情页展示
def detail(request, id):
    resource = Resource.objects.get(id=id)
    r = {}
    r["name"] = resource.name
    r["time"] = resource.up_time.strftime("%Y-%m-%d")
    r["size"] = resource.size
    r["ext"] = resource.ext
    r["keyword"] = resource.resource_key.split(" ")
    for i in r["keyword"]:
        if i == " ":
            r["keyword"].remove(i)
    r["text"] = resource.resource_text
    r["score"] = resource.resource_score
    r["down_num"] = resource.download_num
    user_id = resource.user_id
    r["user_id"] = User.objects.get(id=user_id).info.id
    r["user_name"] = User.objects.get(id=user_id).info.nickname

    comment = Comment.objects.filter(resource_id=id)
    c_ = {}
    c = []

    for i in comment:
        user_info = User.objects.get(id=i.com_user_id).info
        c_["name"] = user_info.nickname
        c_["id"] = user_info.id
        c_["time"] = i.com_time
        c_["star"] = range(0, i.star)
        c_["white_star"] = range(i.star, 5)
        c_["text"] = i.com_text
        c.append(c_)
        c_ = {}
    return render(request, "detai.html", {"resource": r, "comment": c, "num": len(c)})
