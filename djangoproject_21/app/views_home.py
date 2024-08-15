from django.shortcuts import redirect, render 

# 跳转至home界面 
def home(request):
    # 获取session的数据
    useraccount = request.session.get('username',None)
    # 如果用户没有登录，则session中没有useraccount账号，无法进入home页
    if not useraccount:
        # 跳转至登录界面
        return redirect('/app/login')
    # 已登录，跳转home页
    else:
        # 请求转发跳转至home页面
        return render(request,'home.html',{'useraccount':useraccount})

# def gotoHome(request):
#     return render(request,'home.html')