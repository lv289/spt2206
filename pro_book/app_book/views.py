from django.shortcuts import render,HttpResponse,redirect,reverse
from app_book.models import Press,Book,Author
from django.views import View
from django.http import JsonResponse
# Create your views here.
import time
import json
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def det(f):
    def fun(*args,**kwargs):
        start = time.time()
        res = f(*args,**kwargs)
        end = time.time()
        print(f"运行的时长为：{end-start}")
        return res
    return fun


# 出版社查询
def press(request):
    # 去数据库中查询所有出版社信息
    ret = Press.objects.all()  # select * from press;

    return render(request,'press_list.html',{'ret':ret})


# 出版社添加
# def press_add(request):
#     # 接收浏览器发送给后端的数据
#     if request.method =="POST":
#         # 1. 接收数据
#         press_name = request.POST.get('press_name')
#         print(press_name)
#         # 2. 将数据保存到数据库
#         Press.objects.create(name=press_name)
#         # 3. 跳转到press_list界面
#         return redirect('/press_list/')
#     return render(request,"press_add.html")

# CBV
class AddPress(View):


    def get(self,request):
        return render(request, "press_add.html")


    def post(self,request):
        press_name = request.POST.get('press_name')
        print(press_name)
        # 2. 将数据保存到数据库
        Press.objects.create(name=press_name)
        # 3. 跳转到press_list界面
        return redirect(reverse('press'))



# 出版社删除
def press_del(request):
    # 1. 获取要删除的出版社ID
    delete_id = request.GET.get('id')
    # 2. 根据ID，去数据库中删除
    Press.objects.filter(id=delete_id).delete()
    # 3. 返回出版社界面
    return redirect('/press_list/')


# 出版社修改
def press_edit(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        edit_name = request.POST.get("press_name")
        # 2. 去数据库中查找对应的数据对象
        edit_press_new = Press.objects.get(id=edit_id)
        edit_press_new.name = edit_name
        # 修改同步数据库
        edit_press_new.save()
        # return redirect("/press_list/")
        return redirect(reverse('app01:press'))  # ('press_lis')
    #1. 先获取id
    edit_id = request.GET.get('id')
    #2. 去数据库中查询
    ret = Press.objects.filter(id=edit_id)[0]
    return render(request,'press_edit.html',{'press_obj':ret})


# 书的增
def book(request):
    # 数据库中取数据  # select * from book;
    data = Book.objects.all()
    # first_book = data[0]
    # print(data[0])
    # print(first_book.title)
    # print(first_book.press_id)
    # ret2 = Press.objects.get(id=first_book.press_id)
    # print(ret2.name)
    # print(first_book.press)
    # print(first_book.press.name)
    return render(request, 'book_list.html',{"data":data})


# 书的增加
def book_add(request):
    if request.method == "POST":
        book_title = request.POST.get("title")
        press_id = request.POST.get("press_id")
        Book.objects.create(title=book_title,press_id=press_id)
        return redirect("/book_list/")

    press_data = Press.objects.all()
    return render(request,'book_add.html',{"press_list":press_data})


# 书的删除
def book_del(request):
    delete_id = request.GET.get("id")
    Book.objects.filter(id=delete_id).delete()
    return redirect("/book_list/")


# 书的修改
def book_edit(request):
    edit_book_id = request.GET.get("id")
    edit_book_obj = Book.objects.get(id=edit_book_id)
    press_data = Press.objects.all()
    if request.method == "POST":
        new_title = request.POST.get('book_title')
        new_press_id = request.POST.get("press_id")

        edit_book_obj.title = new_title
        edit_book_obj.press_id = new_press_id
        edit_book_obj.save()
        return redirect("/book_list/")

    return render(request,'book_edit.html',{
                    "book_obj":edit_book_obj,
                    "press_list":press_data
                                    })


# 作者
def author(request):
    author_data = Author.objects.all()
    # print(author_data)
    # print(author_data[4].books) # orm桥梁 帮助我们找对应关系
    # print(author_data[4].books.all())

    return render(request,'author_list.html',{"author_list":author_data})


# 作者添加
def author_add(request):
    book_data = Book.objects.all()
    if request.method == "POST":
        new_author_name = request.POST.get('author_name')
        book_ids = request.POST.getlist('books')

        author_obj = Author.objects.create(name=new_author_name)
        author_obj.books.add(*book_ids)
        # author_obj.books.set(book_ids)
        return redirect('/author_list/')
        # return redirect('https://www.baidu.com')
    return render(request,'author_add.html',{"book_list":book_data})


# 作者删除
def author_del(request):
    delete_id = request.GET.get("id")
    Author.objects.filter(id=delete_id).delete()
    return redirect("/author_list/")


# 作者修改
def author_edit(request):
    edit_author_id = request.GET.get("id")
    edit_author_obj = Author.objects.get(id=edit_author_id)
    book_list = Book.objects.all()
    if request.method == "POST":
        new_author_name = request.POST.get("author_name")
        new_book_ids = request.POST.getlist("book_ids")

        edit_author_obj.name = new_author_name
        edit_author_obj.save()
        edit_author_obj.books.set(new_book_ids)
        return redirect("/author_list/")

    return render(request,'author_edit.html',{"author":edit_author_obj,
                                              "book_list":book_list
                                              })







def my_temp(request):

    name = "海等"

    dic = {"name":"rose","age":28}

    class A():
        def __init__(self):
            self.name11 = "bobo"

        def name(self):
            return "我是类中的_name方法"


    def my_print():

        return "hello_my_print"

    li = [my_print,A,dic]
    num = 200000
    buf = "<a href="">百度</a>"
    buf2 = "helloworld!!!66668888000"
        # {"dic":dic,"a":a,"li":li}
    return render(request,'base.html',locals())


def my_demo(request):
    # print(request.path)
    # print(request.body)
    # print(request.method)
    # print(request.POST)
    # print(request.GET)
    # print(request.GET.get("name"))
    # print(request.scheme)
    dic = {"name":"rose","age":20}
    # res = json.dumps(dic)
    # print(request.encoding)
    # print(request.META)
    # print(request.user)

    print(request.get_host())
    print(request.get_full_path())
    print(request.is_secure())
    return JsonResponse([1,2,3],safe=False)
    # print(type(res))
    # return HttpResponse([1,2,3])
    # response = HttpResponse()
    # response["content_type"] = "text/plain/lwq"
    # print(response.content)
    # print(response.status_code)
    # return response






def my_route(request):

    return HttpResponse("my_route")

def my_route2(request):

    return HttpResponse("my_route2")


def my_route3(request,year=2000,month=1):

    return HttpResponse(f"my_route3-{year}-{month}")




def md_test(request):
    print("我是views中的md_test")
    ret = HttpResponse("OK")
    ret.render = render
    return ret
    # return ret

def tr_file(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        file_obj = request.FILES.get("file_name")
        with open("xxx.jpg","wb") as f:
            for line in file_obj:
                f.write(line)


    return render(request,"file.html")

import json
def cal(request):

    print(request.body) # 请求报文的请求体
    print(request.POST)


    return render(request,'cal.html')


def login_requird2(fn):
    def inner(request,*args,**kwargs):
        next = request.path_info
        print(next)
        # if not request.get_signed_cookie('lv_islogin',salt="hello", default=None,max_age=60*60*24*14) == "1":
        if not request.session.get('islogin',None) == '1':
            return redirect('/login/?next={}'.format(next))
        ret = fn(request,*args,**kwargs)
        return ret
    return inner



def login(request):
    if request.method =="POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "lv" and pwd =="123":
            next = request.GET.get('next')
            if next:
                ret = redirect(next)
            else:
                ret = redirect('/index1/')
            # ret.set_signed_cookie("lv_islogin",'1',salt="hello")
            request.session['islogin'] = '1'
            return ret
    return render(request,'login.html')


@login_required
def index1(request):

    return render(request,'index1.html')

@login_required
def home(request):

    return render(request,'home.html')

# @login_requird
def shop(request):

    return HttpResponse("<h1>欢迎访问shop界面</h1>")

def out(request):
    ret = redirect('/login/')
    # ret.delete_cookie('lv_islogin')
    del request.session['islogin']

    return ret

from  django.core.paginator import Paginator

def page(request,pindex):
    orm_data = Author.objects.all()
    paginator = Paginator(orm_data,3) # 每页显示3条数据
    if pindex == '':
        pindex = 1
    else:
        pindex = int(pindex)
    page = paginator.page(pindex) # 实例化第一页这个对象

    return render(request,'page.html',{'page':page})


from django import forms
# form 组件
class MyForm(forms.Form):
    user = forms.CharField(label="用户名",
                           min_length=6,
                           error_messages={
                               'required': '用户名不能为空',
                               "min_length":"short"
                           }

                           )
    pwd = forms.CharField(label="密码")

    gender = forms.fields.ChoiceField(
    # choices = Press.objects.all().values_list("id","name"),
    label = "性别",
    initial = 3,
    widget = forms.widgets.Select() )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['gender'].choices = Press.objects.all().values_list("id","name")


def my_form(request):
    form_obj = MyForm()


    return render(request,'my_form.html',{"form_obj":form_obj})


from django.contrib import auth

def my_auth(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        print(user,pwd)
        user = auth.authenticate(request,username=user,password=pwd)
        if user:
            auth.login(request,user)
            return render(request,'index1.html')

    return render(request,'login.html')


def my_logout(request):
    auth.logout(request)
    return redirect('/my_auth/')






