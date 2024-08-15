import os
from ast import Store
from django.shortcuts import render,redirect
from http.client import HTTPResponse
from app.models import store
import json
from django.http import  JsonResponse
import xlrd
import openpyxl
from django.utils.crypto import get_random_string
from django.http import HttpResponse

def index(request):
    #return render(request,'store.html')
    return queryAllStore(request)
#去store1.html
def gotoStore1(request):
    return render(request,'store1.html')




# 查询全部仓库信息
def queryAllStore(request):
    # 查询Store表的全部记录
    lstStore=store.objects.all()
    # 封装到传递参数中
    context=dict()
    context['lstStore']=lstStore
    # 页面响应跳转
    return render(request,'store_normal.html',context)

# 查询特定名称仓库
def searchCertainStore(request):
    # print(123)
    print(123)
    
    searchName=request.POST.get('inquirystoreName','')
    searchLoca=request.POST.get('inquirystoreLoca','')
    searchType=request.POST.get('inquirystoreType','')
    context2=dict()
    print(searchName)
    print(searchLoca)
    print(searchType)
    # if(searchLoca==''):
    #     searchLoca=None
    
    getId=[] 
    getId=store.objects.filter(storeName__icontains=searchName,storeLoca__icontains=searchLoca,storeType__icontains=searchType)
    print(getId)
    context2['lstStore']=getId
    return render(request,'storeSearch_normal.html',context2)

