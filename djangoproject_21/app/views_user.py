from ast import Store
from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import render
from app.models import user,store,goods
from django.http import  JsonResponse
from app import views

def gotoUserInfo(request):
    userInfo(request)
    return render(request,'userInfo.html')


def userInfo(request):
    print("获取用户信息")
    useraccount=request.session.get('username')
    # lstStore=user.objects.filter(useraccount_iexact=useraccount)
    Name=user.objects.filter(useraccount = useraccount).values('usedName')# 返回id对应的姓名
    Age=user.objects.filter(useraccount = useraccount).values('userage')
    Sex=user.objects.filter(useraccount = useraccount).values('userSex')
    Number=user.objects.filter(useraccount = useraccount).values('userNumber')
    Tel=user.objects.filter(useraccount = useraccount).values('usertel')
    Dept=user.objects.filter(useraccount = useraccount).values('userDept')
    Role=user.objects.filter(useraccount = useraccount).values('userRole')
    Account=user.objects.filter(useraccount = useraccount).values('useraccount')
    Address=user.objects.filter(useraccount = useraccount).values('useraddr')
    Class=user.objects.filter(useraccount = useraccount).values('userClass')
    #因为这里得到的变量是queryset类型，先转为list类型，再取得list中的第一对象是dict类型，再从dict中取得所需内容
    Age=list(Age)
    Age=Age[0]
    Name=list(Name)
    Name=Name[0]
    Sex=list(Sex)
    Sex=Sex[0]
    Number=list(Number)
    Number=Number[0]
    Tel=list(Tel)
    Tel=Tel[0]
    Dept=list(Dept)
    Dept=Dept[0]
    Role=list(Role)
    Role=Role[0]
    Account=list(Account)
    Account=Account[0]
    Address=list(Address)
    Address=Address[0]
    Class=list(Class)
    Class=Class[0]
    print(Age)
    
    print(Address)
    print()
    #print(Loca['storeLoca'])
    data=dict()
    # 打包成dict传回去
    data['用户名']=Account['useraccount']
    data['姓名'] = Name['usedName']
    data['年龄']=Age['userage']
    data['性别']=Sex['userSex']
    data['工号']=Number['userNumber']
    data['电话']=Tel['usertel']
    data['部门']=Dept['userDept']
    data['用户权限']=Role['userRole']
    # data['showuserRole']=Role['userRole']
    data['地址']=Address['useraddr']
    data['用户类型']=Class['userClass']
    #print(data['showstoreCap'])
    print(data)
    
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
    return render(request,'userInfo.html',{'search_list': search_list,'searchGoods_list':searchGoods_list,'data': data})


def index(request,data):
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
    return render(request,'userInfo.html',{'search_list': search_list,'searchGoods_list':searchGoods_list,'data': data})



    # print(data)
    # return JsonResponse(data)
"""
def userInfo(request):
    print(123)
    useraccount=request.session.get('useraccount')
    # lstStore=user.objects.filter(useraccount_iexact=useraccount)
    Name=user.objects.filter(useraccount = useraccount).values('userName')# 返回id对应的姓名
    Age=user.objects.filter(useraccount = useraccount).values('userage')
    Sex=user.objects.filter(useraccount = useraccount).values('userSex')
    Number=user.objects.filter(useraccount = useraccount).values('userNumber')
    Tel=user.objects.filter(useraccount = useraccount).values('usertel')
    Dept=user.objects.filter(useraccount = useraccount).values('userDept')
    Role=user.objects.filter(useraccount = useraccount).values('userRole')
    Account=user.objects.filter(useraccount = useraccount).values('useraccount')
    Address=user.objects.filter(useraccount = useraccount).values('useraddr')
    Class=user.objects.filter(useraccount = useraccount).values('userClass')
    #因为这里得到的变量是queryset类型，先转为list类型，再取得list中的第一对象是dict类型，再从dict中取得所需内容
    Age=list(Age)
    Age=Age[0]
    Name=list(Name)
    Name=Name[0]
    Sex=list(Sex)
    Sex=Sex[0]
    Number=list(Number)
    Number=Number[0]
    Tel=list(Tel)
    Tel=Tel[0]
    Dept=list(Dept)
    Dept=Dept[0]
    Role=list(Role)
    Role=Role[0]
    Account=list(Account)
    Account=Account[0]
    Address=list(Address)
    Address=Address[0]
    Class=list(Class)
    Class=Class[0]
    print(Age)
    print(type(Age))
    print(Address)
    print()
    #print(Loca['storeLoca'])
    data=dict()
    # 打包成dict传回去
    data['用户名']=Account['useraccount']
    data['姓名'] = Name['userName']
    data['年龄']=Age['userage']
    data['性别']=Sex['userSex']
    data['工号']=Number['userNumber']
    data['电话']=Tel['usertel']
    data['部门']=Dept['userDept']
    data['用户权限']=Role['userRole']
    # data['showuserRole']=Role['userRole']
    data['地址']=Address['useraddr']
    data['用户类型']=Class['userClass']
    #print(data['showstoreCap'])
    print(data)
    return render(request,'userInfo copy.html',{'data': data})
"""