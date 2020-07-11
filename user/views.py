from django.shortcuts import render, redirect
from .models import User, User_info
from django.http import HttpResponse
import json
from hashlib import md5
from .forms import UserForm, UserInfoForm


# Create your views here.

def reg(request):
    return render(request, "register.html")


def reg2(request):
    user = request.POST.dict()
    # password = user["password"]
    # m = md5()
    # m.update(password.encode())
    # password = m.hexdigest()
    # User.objects.create(username=user["username"], password=password)
    return render(request, "register2.html", {"user": user})


# 账户数据库录入
def reg3(request):
    # 获取表单参数
    user_dict = request.POST.dict()
    # 获取文件
    photo = request.FILES.get("photo")
    photo = photo.read()
    # 提取账户密码
    user_u_p = eval(user_dict["u_p"])
    # 密码加密
    password = user_u_p["password"]
    m = md5()
    m.update(password.encode())
    password = m.hexdigest()
    # 存入数据库
    User.objects.create(username=user_u_p["username"], password=password)
    # 获取用户id
    user_id = User.objects.filter(username=user_u_p["username"])[0].id

    User_info.objects.create(nickname=user_dict["nickname"], realname=user_dict["realname"],
                             user_email=user_dict["email"], user_phone=user_dict["tel"],
                             sex=user_dict["sex"], photo=photo, user_id=user_id)

    return render(request, "register3.html")


# 账户注册验证
def check_user(request):
    print(request.POST.dict()["username"])

    user = User.objects.filter(username=request.POST.dict()["username"])
    if len(user) == 0:
        status = 200
    else:
        status = 500
    msg = json.dumps({"status": status})
    return HttpResponse(msg)


# 登陆验证
def login(request):
    user = request.POST.dict()
    m = md5()
    m.update(user["password"].encode())
    password = m.hexdigest()
    user_ = User.objects.filter(username=user["username"], password=password)
    if len(user_) == 0:
        msg = json.dumps({"status": 500})
        return HttpResponse(msg)
    else:

        info = user_[0].info
        info.photo = None
        form = UserInfoForm(instance=info)
        form.is_valid()
        info = form.initial
        request.session["user"] = info
        return redirect("/")


def modifypass(request):
    return render(request, "modifypass.html")


# 调取图片
def show_photo(request, id):
    # 读取流文件
    photo = User_info.objects.filter(id=id).first().photo
    return HttpResponse(photo)


def check_pwd(request):
    user = User.objects.get(id=request.session["user"]["user"])
    o_pwd = request.POST.dict()["o_pwd"]
    m = md5()
    m.update(o_pwd.encode())
    m = m.hexdigest()
    if user.password == m:
        msg = {"status": 200}
    else:
        msg = {"status": 500}
    msg = json.dumps(msg)
    return HttpResponse(msg)

def change_pwd(request):
    pwd = request.POST.dict()["password"]
    m = md5()
    m.update(pwd.encode())
    password = m.hexdigest()
    User.objects.filter(id=request.session["user"]["user"]).update(password=password)

    return redirect(to="/")