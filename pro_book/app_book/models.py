from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 出版社表
class Press(models.Model):
    id = models.AutoField(primary_key=True)  # id 主键
    name = models.CharField(max_length=32)  # 出版社名称  CharField == SQL(varchar)

    def __str__(self):
        return f"这是Press对象-{self.name}"

# 书表
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    press = models.ForeignKey(to='Press',on_delete=models.CASCADE)

    def __str__(self):
        return f"这是Book对象-{self.title}"


# 作者表--》orm自动创建
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32) # 作者名
    books = models.ManyToManyField(to='Book')

    def __str__(self):
        return f"这是Author对象-{self.name}"

# 多对多的关系，必须有第三张表-第一种方式
# class AuthorToBook(models.Model):
#     id = models.AutoField(primary_key=True)
#     author = models.ForeignKey(to='Author',on_delete=models.CASCADE)
#     book = models.ForeignKey(to='Book',on_delete=models.CASCADE)


class Stu(models.Model):
    stu_name = models.CharField(max_length=32) # 作者名
    bir = models.DateField(auto_now_add=True,db_index=True)
    sex = models.BooleanField()
    # 2020.12   100000.00
    price = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    dept = models.CharField(max_length=32,default="人事部")
    shop_num = models.CharField(max_length=32, default="100")
    res_num2 = models.CharField(max_length=32, default="0")

    def __str__(self):
        return f"这是Stu对象-{self.stu_name}"

    # 空 和 NULL的区别

class MyUser(models.Model):
    user = models.CharField(max_length=32,)
    pwd = models.CharField(max_length=32, )


class UserInfo(AbstractUser):

    iphone = models.CharField(max_length=11)

    def __str__(self):
        return self.username
