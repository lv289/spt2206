from django.urls import path, re_path
from app_book.views import *


urlpatterns = [

    # path('index/',index,name='zx_index'),
    path('my_temp/',my_temp),
    path('my_demo/', my_demo),
    # 出版社增删改查
    # 第一个参数-url，第二个参数 视图函数名
    path('press_li/',press,name='press'),
    # path('press_add/',press_add),
    path('press_add/',AddPress.as_view()),
   # path('press_add/', AddPress.view),
    path('press_del/',press_del),
    path('press_edit/',press_edit),

    # 书的增删改查
    path('book_list/', book,),
    path('book_add/', book_add),
    path('book_del/', book_del),
    path('book_edit/', book_edit),

    # 作者
    path('author_list/', author),
    path('author_add/', author_add),
    path('author_del/', author_del),
    path('author_edit/', author_edit),


    # django v1版本的 url == re_path
    # 路由匹配规则：
    #   1.从上往下，只有有匹配上的，那么后边的路由就不再进行匹配
    #   2. 如果路由中有小括号。把括号中的匹配内容当作参数传递给视图函数
    # http://192.168.0.103:8000/lv/2022/09
    re_path(r"lwq/$",my_route3),
    re_path(r"lv/\d{4}/\d{2}", my_route2),
    re_path(r"lwq/(?P<year>\d{4})/(?P<month>\d{2})", my_route3),  # 分页

    path('lv_md/', md_test),
    path('tr_file/', tr_file),
    path('cal/', cal),

    path('login/', login),
    path('index1/', index1),
    path('home/', home),
    path('out/', out),
    path('shop/', shop),
    re_path(r'page(?P<pindex>\d*)/', page),
    path('my_form/', my_form),

    path('my_auth/', my_auth),
    path('my_logout/', my_logout),
]
