# from ast import Store
from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import render
# from app.models import store

from django.shortcuts import render
from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import  JsonResponse
from app.models import store,user,goods
import json

# from app.models import store
from app.views_notice import get_read_notifications, get_unread_notifications



def gotoHello(request):
    return render(request, 'hello.html')


def goto_unread(request):
    get_unread_notifications(request)
    return render(request, 'notifications_unread.html')


def goto_read(request):
    get_read_notifications(request)
    return render(request, 'notifications_read.html')

def index(request):
    print(123)
    # 查询出Person对象信息，也就是数据表中的所有数据
    # 一行数据就是一个对象，一个格子的数据就是一个对象的一个属性值
    # objs = Person.objects.all()
    # print(objs)
    # # locals函数可以将该函数中出现过的所有变量传入到展示页面中，即index.html文件中
    # return render(request,'index3.html',locals())
    search_list = dict()
    searchGoods_list=dict()
    type = store.objects.values_list('storeLoca',flat=True)
    typeGoods = goods.objects.values_list('goodsType',flat=True)
    type_list = list(type)
    type_set = set(type_list)
    typeGoods_list = list(typeGoods)
    typeGoods_set = set(typeGoods_list)
    try:
        for i in type_set:
            count = type_list.count(i)
            # print("the %s has found %d" %(i,type_list.count(i)))
            # tem = {}
            # tem['name'] = i
            # tem['value'] = count
            
            search_list[i]=count
        print('search_list:---',search_list)
    except Exception as e:
        print('e:',e)
    

    try:
        for i in typeGoods_set:
            count = typeGoods_list.count(i)
            # print("the %s has found %d" %(i,type_list.count(i)))
            # tem = {}
            # tem['name'] = i
            # tem['value'] = count
            
            searchGoods_list[i]=count
        print('searchGoods_list:---',searchGoods_list)
    except Exception as e:
        print('e:',e)
    return render(request,'test_save.html',{'search_list': search_list,'searchGoods_list':searchGoods_list})

