from ast import Store
from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.shortcuts import render
from app.models import user

# def infor(request): 
#     if request.POST:
#         # userId=request.POST.get('userId',None)
#         # userName=request.POST.get('userName',None)
#         # userPassword=request.POST.get('userPassword',None)
#         userRole=request.POST.get('userRole',None)
#         userClass=request.POST.get('userClass',None)
#         userNumber=request.POST.get('userNumber',None)
#         userSex=request.POST.get('userSex',None)
#         userDept=request.POST.get('userDept',None)
#         try:
#             # user.objects.create(userId=userId)
#             # user.objects.create(userName=userName)
#             user.objects.create(userRole=userRole)
#             # user.objects.create(userPassword=userPassword)
#             user.objects.create(userNumber=userNumber)
#             user.objects.create(userSex=userSex)
#             user.objects.create(userDept=userDept)
#             # 响应客户端
#             return ##到每个地方
#             # return render(request,'addStore.html',{'message':'[OK].数据添加成功.'})

#         except:
#             # 响应客户端
#             return render(request,'home.html',{'message':'[Error].数据添加失败.'})

#     else:
#         # 响应客户端
#         return render(request,'home.html')
def gotoRegister(request):
    return render(request,"register.html")

def register(request):
    if request.POST:
        useraccount = request.POST.get('username', None)
        userSex = request.POST.get('gender', None)
        usedName = request.POST.get('name', None)
        userage = request.POST.get('age', None)
        usertel = request.POST.get('tel', None)
        useraddr = request.POST.get('address', None)
        userRole = request.POST.get('work', None)
        userDept = request.POST.get('department', None)
        userClass = request.POST.get('usertype', None)
        userPassword = request.POST.get('password', None)
        userNumber = request.POST.get('nums', None)
        email="123@123.com"
        try:
            print("before try")
            user.objects.create_superuser(useraccount=useraccount, userSex=userSex, usedName=usedName, userage=userage,username=useraccount,
                                    usertel=usertel, useraddr=useraddr, userRole=userRole, userDept=userDept,
                                    userClass=userClass, userPassword=userPassword, userNumber=userNumber,password=userPassword,email=email)
            print("creat success")
            return render(request, 'register.html',{"regi_success_msg":"注册成功！请返回登录！"})  # 到每个地方

                # return render(request,'addStore.html',{'message':'[OK].数据添加成功.'})

        except:
            # 响应客户端
            print("except")
            return render(request, 'register.html', {'regi_error_msg': '[Error].用户名已存在！注册失败！'})

    else:
        return redirect("/app/login/")

