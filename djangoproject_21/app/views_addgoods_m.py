from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.models import goods,store
from app.views_notice import send_notifications

# 进入添加物料信息界面（未登录限制进入）
def goto_addgoods_mobile(request):
    # 获取session的数据
    useraccount = request.session.get('username',None)
    # 如果用户没有登录，则session中没有useraccount账号，无法进入home页
    if not useraccount:
        # 跳转至登录界面
        return redirect('/app/login_mobile')
    # 已登录，跳转home页 
    else:
        print("ready to addgoods.html")
        # 请求转发跳转至home页面
        return render(request,'addgoods.html',{'useraccount':useraccount})

# 添加物料信息
def addgoods_mobile(request):
    if request.POST:
        # 接收请求数据
        goodsType=request.POST.get('addGoodsType',None)# 这里可以在前端设置有哪些选项
        goodsName=request.POST.get('addGoodsName',None)# 这里可以在前端设置有哪些选项
        goodsStore=request.POST.get('addGoodsStore',None)# 这里可以在前端设置有哪些选项
        # goods_lastStore=request.POST.get('goods_lastStore',None)# 这里可以在前端设置有哪些选项
        # goods_date=request.POST.get('goods_date',None)
        goodsAmount=request.POST.get('addGoodsAmount',None)
        goodsShelves=request.POST.get('addGoodsShelves',None)
        goodsStore=store(goodsStore)
        try: 
            # 存储响应内容
            goods.objects.create(goodsType=goodsType,goodsName=goodsName,goodsStore=goodsStore,goodsShelves=goodsShelves,goodsAmount=goodsAmount)
            print("ready to send")
                #通知内容
            send_notifications(sender=request.user, verb='添加货物 ' + goodsName + ' 到仓库 ' + goodsStore.storeName,
                            receiver='仓库管理员')
            print("ready to print")
            print(request.user.notifications.unread())
            # goods.objects.create(goodsName=goodsName)
            # goods.objects.create(goodsStore=goodsStore)
            # goods.objects.create(goodsShelves=goodsShelves)
            # # goods.objects.create(goods_date=goods_date)
            # goods.objects.create(goodsAmount=goodsAmount)
            # 响应客户端
            
            print("ready to return")
            return render(request,'addgoods.html',{"success_msg":"物料添加成功！"})
            # return render(request,'addStore.html',{'message':'[OK].数据添加成功.'})

        except:
            # 响应客户端
            return render(request,'addgoods.html',{"success_msg":"物料添加成功！"})

    else:
        # 响应客户端
        return render(request,'addgoods.html')