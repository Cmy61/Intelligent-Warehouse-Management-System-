from traceback import print_tb
from django.shortcuts import redirect, render
from http.client import REQUEST_URI_TOO_LONG, HTTPResponse
from django.shortcuts import render
from django.shortcuts import render
from app.models import user
from django.contrib import auth
from django.shortcuts import redirect, render
from http.client import REQUEST_URI_TOO_LONG, HTTPResponse
from django.shortcuts import render
from django.shortcuts import render
from app.models import user
from django.contrib import auth
from django.template import RequestContext
from django.http import HttpResponseRedirect
# def gotoLogin(request):
#     return render(request, 'login.html')

#登录账号(移动端)
def login_mobile(request):

    if request.POST:
        # 接收客户端请求数据
        useraccount = request.POST.get('username',None)
        userPassword = request.POST.get('password',None)
        lstuser = user.objects.filter(useraccount__exact = useraccount, userPassword__exact = userPassword).values('userClass')
        #因为这里得到的变量是queryset类型，先转为list类型，再取得list中的第一对象是dict类型，再从dict中取得所需内容
        if lstuser:
            lstuser=list(lstuser)
            lstuser=lstuser[0]
            lstuser=lstuser['userClass']
            if (lstuser=="仓库管理员"):
                print("get account")
                
                # 设置响应路径
                rep = redirect("/app/addgoods_mobile/")
                # 将登录账号加密后写入Cookie中
                rep.set_signed_cookie('username', useraccount, salt='www.chinasofti.com')
                # 登录成功后，将用户账号写入session中
                request.session['username'] = useraccount
                # 响应客户端
                print("ready to return")
                return rep
            else:
                return render(request, 'login_mobile.html',{"error_msg":"您不具备管理员权限！"})
        else: 
            # 响应客户端
            return render(request, 'login_mobile.html',{"error_msg":"账号或密码错误！"})
    else:
        # 从Cookie中获取account的值
        useraccount = request.get_signed_cookie('username', None, salt='www.chinasofti.com')
        # 判断accont是否存在，决定是否补填数据
        if useraccount:
            # 响应客户端，并将account的值传递
            return render(request, 'login_mobile.html', {'username':useraccount})
        else:
            # 响应客户端（页面跳转）
            return render(request, 'login_mobile.html')



# 登录账号(Web端)
def login(request):
    
    if request.POST:
        # 接收客户端请求数据
        useraccount = request.POST.get('username',None)
        userPassword = request.POST.get('password',None)
        userPassword1=request.POST.get('password',None)
        lstuser = user.objects.filter(useraccount__exact = useraccount, userPassword__exact = userPassword)
        
        if lstuser:
            print("lstuser网页符合")
            userPassword=lstuser.values("password")
            userPassword=list(userPassword)
            userPassword=userPassword[0]
            print("userPassword:",userPassword['password'])
            print("userPassword1:",userPassword1)
            user1 = auth.authenticate(username=useraccount, password=userPassword1)
            if user1 :
                print("user1网页符合")
                auth.login(request, user1)  # 登录
                request.session['user'] = useraccount  # 将session信息记录到浏览器
                response = HttpResponseRedirect('/app/user/')
                rep = redirect("/app/user/")
                # 将登录账号加密后写入Cookie中
                rep.set_signed_cookie('username', useraccount, salt='www.chinasofti.com')
                # 登录成功后，将用户账号写入session中
                request.session['username'] = useraccount
                # 响应客户端
                return response
            else:
                print("user1网页不符合")
                return render(request, "login.html")
            # 设置响应路径
        else:
            # 响应客户端
            return render(request, 'login.html',{"error_msg":"账号或密码错误！"})
    else:
        # 从Cookie中获取account的值
        useraccount = request.get_signed_cookie('username', None, salt='www.chinasofti.com')
        # 判断accont是否存在，决定是否补填数据
        if useraccount:
            # 响应客户端，并将account的值传递
            return render(request, 'login.html', {'username':useraccount})
        else:
            # 响应客户端（页面跳转）
            return render(request, 'login.html')