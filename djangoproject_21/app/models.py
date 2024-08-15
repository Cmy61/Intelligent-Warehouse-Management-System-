from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models
import datetime
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser,User
from django.db import models
from django.utils import timezone
#仓库
class store(models.Model): 
    storeId = models.AutoField(primary_key=True)# 自动增长，主键
    storeName = models.CharField(max_length=30)# 定义长度为30的字符串
    storeType = models.CharField(max_length=30)# 这里可以在前端设置有哪些选项
    storeLoca = models.CharField(max_length=30)# 这里可以在前端设置有哪些选项
    storeCap = models.DecimalField(max_digits=10, decimal_places=2) # 容积大小，单位备注为吨
    # storeExist = models.DecimalField(max_digits=10, decimal_places=2, default=0) # 已使用容积
    pass

# 货架
class shelves(store):
    shelvesId = models.AutoField(primary_key=True) # 自动增长，主键
    shelvesNum = models.CharField(max_length=30) # 货架编号，可自定义名称为cqL01-A1号 重庆大型一号仓库A区1号货架
    shelvesArea = models.CharField(max_length=30) # 货架所在区域（A、B、C、D四个区域）
    shelvesGoods = models.CharField(max_length=30) # 货架放置的货物类型
    shelvesStore = models.ForeignKey(store,on_delete=models.CASCADE,related_name='Store_shelves') # 将货架与仓库关联
    shelvesDisinfect = models.CharField(max_length=30) # 货架是否消毒

# 物料
class goods(models.Model):
    goodsId = models.AutoField(primary_key=True)# 自动增长，主键
    goodsType = models.CharField(max_length=30) # 
    goodsName = models.CharField(max_length=30) # 货物名称
    # 将货物与storeId联系在一起
    goodsStore = models.ForeignKey(store,on_delete=models.CASCADE,related_name='Store_goods')# 删除主键记录和相应的外键表记录
    #goodsStore = models.CharField(max_length=30) # 
    # goods_lastStore = models.CharField(max_length=30) # 
    goodsDate=models.DateTimeField(default=timezone.now())
    goodsAmount=models.DecimalField(max_digits=10, decimal_places=2)
    #goodsShelves = models.ForeignKey(shelves,on_delete=models.CASCADE,related_name='Shelves_goods') # 将货物关联货架
    goodsShelves=models.CharField(max_length=30)
    pass
    # goodsTime =



# 用户
class user(AbstractUser):
    userId = models.AutoField(primary_key=True)  # 自动增长，主键
    useraccount = models.CharField(max_length=30, unique=True)
    userSex = models.CharField(max_length=30)
    usedName = models.CharField(max_length=30)  #
    userage = models.CharField(max_length=30)
    usertel = models.CharField(max_length=30)
    useraddr = models.CharField(max_length=30)
    userRole = models.CharField(max_length=30)  #
    userDept = models.CharField(max_length=30)
    userClass = models.CharField(max_length=30)
    userPassword = models.CharField(max_length=30)  #
    userNumber = models.CharField(max_length=30)
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
    pass
