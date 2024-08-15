from django.shortcuts import redirect, render

# 退出账号
def logout(request):
    # 删除当前登录者的session中的信息
    del request.session['username']
    print('删除当前登录者的信息')
    # 重定向至登录页面
    return redirect('/app/login/')