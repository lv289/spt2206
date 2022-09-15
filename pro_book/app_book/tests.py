from django.test import TestCase

# Create your tests here.

import os
from pymysql import connect
if __name__ == '__main__':

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pro_book.settings")
    import django
    django.setup()
    from app_book.models import Book,Press,Author,Stu
    from django.db.models import Avg, Sum, Max, Min, Count, F, Q

    # # 增删改查
    # Stu.objects.create(stu_name="rose",bir="2001-08-10")

    # stu_obj = Stu.objects.create(stu_name="tom",sex=1,price=20)
    # stu_obj = Stu.objects.filter(stu_name="tom").update(stu_name="jack")
    # stu_obj = Stu.objects.all() # queryset集合
    # stu_obj = Stu.objects.get(bir="2022-09-05")  # 对象。
    # stu_obj = Stu.objects.filter(id=3) #  queryset集合,查询不到不报错。<QuerySet []>
    # stu_obj = Stu.objects.exclude(bir="2022-09-05")  # <QuerySet []>
    # stu_obj = Stu.objects.filter(id=1).values("stu_name")
    # stu_obj = Stu.objects.values_list("stu_name")
    # select stu_name from stu;
    # stu_obj = Stu.objects.all().order_by("-id")
    # book_obj = Book.objects.values("press_id").distinct()
    # book_obj = Book.objects.all().count()
    # book_obj = Book.objects.all().first()
    # book_obj = Book.objects.filter(id=234).exists()
    # -- select * from stu;
    # ============= 神奇的双下划线===================
    # stu_obj = Stu.objects.filter(price__lt=100)
    # stu_obj = Stu.objects.filter(price__in=[100,20,30,50])
    # stu_obj = Stu.objects.exclude(price__in=[100, 20, 30, 50])
    # stu_obj = Stu.objects.filter(stu_name__icontains="O")
    # stu_obj = Stu.objects.filter(price__range=[100,249])
    # stu_obj = Stu.objects.filter(bir__day=6)
    #
    # print(stu_obj)

    # --------------基于双下划线的跨表查询（join查询）
    """
    正向查询按字段，反向查询按照表名小写用来告诉ORM引擎join哪张表
    """
    # 我们会的 根据西游记图书找对应的出版社
    # press_name = Book.objects.filter(title="西游记").first().press.name
    # press_name2 = Book.objects.filter(title="西游记").values("press__name")
    # press_name3 = Press.objects.filter(book__title="西游记").values("name")
    # press_es = Book.objects.values("press__name")
    # print(press_name)
    # print(press_name2)
    # print(press_name3)
    # print(press_es)

    # # 根据五道口出版社获取对应书名
    # title = Press.objects.filter(name="五道口出版社").values("book__title")
    # print(title)

    # 多对多
    # 通过作者找书名  正向
    # books = Author.objects.filter(name="琼瑶").values("books__title")
    # print(books)
    # 根据人生这本书找对应的作者
    # author_name = Book.objects.filter(title="人生").values("author__name")

    # press_name = Author.objects.filter(name="琼瑶").values("books__press__name")
    # 五道口 --》 作者
    # author_name = Press.objects.filter(name="工业出版社").values("book__author__name")
    # print(author_name)

    # res = Stu.objects.all().aggregate(lv=Avg("price"),max = Max("price"))
    # res = Stu.objects.values("dept").annotate(avg=Count("price"))
    # res = Stu.objects.filter(Q(price__gt=2000) | Q(price__lt=100))
    # print(res)
    res = Stu.objects.filter(shop_num__gt=F("res_num2"))
    print(res)

    from django.db import transaction

    try:
        with transaction.atomic():
            new_publisher = Press.objects.create(name="lv出版社")
            Book.objects.create(name="python基础入门")  # 指定一个不存在的出版社id

    except Exception as e:
        print(e)









