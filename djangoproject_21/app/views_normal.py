import os
from ast import Store
from django.shortcuts import render,redirect
from http.client import HTTPResponse
from app.models import store,user
import json
from django.http import  JsonResponse
import xlrd
import openpyxl
from django.utils.crypto import get_random_string
from django.http import HttpResponse

def trans_goods(request):
    useraccount=request.session.get('username')
    Class=user.objects.filter(useraccount = useraccount).values('userClass')
    #因为这里得到的变量是queryset类型，先转为list类型，再取得list中的第一对象是dict类型，再从dict中取得所需内容
    Class=list(Class)
    Class=Class[0]
    Class=Class['userClass']
    if(Class=="仓库管理员"):
        return redirect('/app/index2/')
    else:
        return redirect('/app/index2_normal/')
    
def trans_store(request):
    useraccount=request.session.get('username')
    Class=user.objects.filter(useraccount = useraccount).values('userClass')
    #因为这里得到的变量是queryset类型，先转为list类型，再取得list中的第一对象是dict类型，再从dict中取得所需内容
    Class=list(Class)
    Class=Class[0]
    Class=Class['userClass']
    if(Class=="仓库管理员"):
        return redirect('/app/index/')
    else:
        return redirect('/app/index_normal/')
    
