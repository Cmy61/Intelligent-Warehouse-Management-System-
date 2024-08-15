from ast import Store
from re import search
from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import render
from app.models import user
from django.http import  JsonResponse
from app.models import shelves

def gotoshelves(request):
    return render(request,'shelves_search.html')

def shelvesinfor(request):
    shelvesNum = request.POST.get('sNum',None) # 获取用户输入的货架编号
    context2=dict()
    shelves_information = []
    shelves_information = shelves.objects.filter(shelvesNum__iexact = shelvesNum)
    context2['lstShelves']=shelves_information
    return render(request,'shelves.html',context2)