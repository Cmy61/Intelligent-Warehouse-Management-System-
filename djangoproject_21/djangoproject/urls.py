"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views,views_goods,views_store,views_login,views_register,views_home,views_cloud,views_logout,views_user,views_goods_normal,views_store_normal,views_normal,views_shelvesinfor
from django.contrib import admin
from django.urls import path, include
from app import views, views_goods, views_store, views_login, views_register, views_home, views_cloud, views_logout, \
    views_user, views_goods_normal, views_store_normal, views_normal, views_shelvesinfor, views_addgoods_m
import notifications.urls
from app import views_notice
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/hello/',views.gotoHello), # 进入欢迎界面
    # path('app/gotologin/',views_login.gotoLogin),
    path('app/login/',views_login.login), # 进入登录界面
    # path('app/login/',views_login_register.gotoLogin),
    # path('app/register/',views_login_register.gotoRegister),
    path('app/gotoregister/',views_register.gotoRegister), # 去注册界面
    path('app/register/',views_register.register), # 注册
    #path('app/home/',views_home.home),
    path('app/home/',views_home.home), # 进入主页
    path('app/index/', views_store.index), # 展示仓库所有信息
    #path('app/store1/',views_store.gotoStore1),
    #path('store1/',views_store.gotoStore1),
    path('app/addStore/add/', views_store.addStore), # 增加仓库信息
    path('app/transStore/trans/<int:id>', views_store.show),
    path('app/updateStore/update/', views_store.updateStore), # 更新仓库信息
    path('app/deleteStore/delete/<int:id>', views_store.deleteStore), # 删除仓库信息
    path('app/searchStore/search/', views_store.searchCertainStore), # 搜索仓库信息
    path('app/cloud/',views_cloud.gotoCloud), # 腾讯云图数据可视化
    path('app/importStore/import/',views_store.import_Sexcel), # 导入仓库信息excel
    path('app/exportStore/export/',views_store.export_store), # 导出仓库信息excel
    path('app/importGoods/import/',views_goods.import_Gexcel), # 导入物料信息excel
    path('app/exportGoods/export/',views_goods.export_goods), # 导出物料信息excel
    path('app/userin/',views_user.gotoUserInfo), # 展示用户信息
    
    path('app/logout/',views_logout.logout), # 退出登录
    path('app/gotoGoods/goto/<int:id>',views_goods.showGoods), # 展示物料信息
    path('app/index2/',views_goods.GoodsStore), # 展示物料所属仓库的所有信息
    path('app/addGoods/add/', views_goods.addGoods), # 增加物料信息
    path('app/deleteGoods/delete/<int:id>', views_goods.deleteGoods), # 删除物料信息
    path('app/searchGoods/search/', views_goods.searchCertainGoods), # 搜索物料信息
    path('app/transGoods/trans/<int:id>', views_goods.show),
    path('app/updateGoods/update/', views_goods.updateGoods), # 更新物料信息
    path('app/gotoGoods_normal/goto/<int:id>',views_goods_normal.showGoods), # 
    path('app/index2_normal/',views_goods_normal.GoodsStore), # 普通员工展示物了所属仓库的所有信息
    path('app/searchGoods_normal/search/', views_goods_normal.searchCertainGoods), # 普通员工查询物料
    path('app/trans_store/',views_normal.trans_store), # 判断身份跳转界面
    path('app/trans_goods/',views_normal.trans_goods), # 判断身份跳转界面
    path('app/index_normal/', views_store_normal.index), # 普通员工展示所有仓库信息
    path('app/searchStore_normal/search/', views_store_normal.searchCertainStore), # 普通员工
    path('app/shelves_search/',views_shelvesinfor.gotoshelves), # 移动端查询货架信息搜索界面
    path('app/shelvesinformation/',views_shelvesinfor.shelvesinfor), # 货架信息结果显示页
    path('app/login_mobile',views_login.login_mobile), # 进入移动端登录页面
    path('app/addgoods_mobile/',views_addgoods_m.goto_addgoods_mobile), # 进入移动端添加货物界面
    path('app/addgoods_mobile_ok/',views_addgoods_m.addgoods_mobile), # 进入移动端添加货物界面
    path('app/notifications/', include(notifications.urls, namespace='notifications')),
    path('app/notifications_unread/', views.goto_unread),
    path('app/notifications_read/', views.goto_read),
    path('update_status/', views_notice.update_status, name="update_status"),
    path('get_unread_notifications/', views_notice.get_unread_notifications, name="get_unread_notifications"),  # 未读消息界面
    path('get_read_notifications/', views_notice.get_read_notifications, name="get_read_notifications"),    # 已读消息界面
    path('app/user/',views_user.userInfo),
]