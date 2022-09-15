from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,HttpResponse,redirect,reverse
import datetime

class MD1(MiddlewareMixin):
    """
    自己实现自定义的中间件
    """
    def process_request(self,request):

        print("我是MD1类中的process_request方法")


    def process_response(self, request, response):

        print("我是MD1类中的process_response方法")
        return response


    def process_view(self, request, view_func, view_args, view_kwargs):
        print("我是MD1类中的process_view方法")



    def process_exception(self, request, exception):
        print("我是MD1类中的process_exception方法")
        print("*" * 50)
        print(exception)
        print("*"*50)

    def process_template_response(self, request, response):
        print("我是MD1类中的process_template_response方法")
        return response


class MD2(MiddlewareMixin):
    """
    自己实现自定义的中间件
    """
    # 设置访问IP池
    IP_DICT = {}

    def process_request(self,request):
        # 1分钟内只能访问3次。
        # 记录每次访问的IP
        ip_name = request.META.get('REMOTE_ADDR')
        # 如果在IP池中执行如下代码
        if ip_name in self.IP_DICT:
            # 获取该IP的超时时间点
            setted_time = self.IP_DICT.get(ip_name).get('time')
            # 当前请求的访问时间点
            now = datetime.datetime.now()
            # 获取访问次数
            visit_count = self.IP_DICT.get(ip_name).get('count')
            # 新的访问次数
            new_count = visit_count + 1
            # 判断 访问次数小于3次,并且当前的访问时间没有超过超时时间，可以继续访问
            if new_count <= 3 and now <= setted_time:
                self.IP_DICT.get(ip_name)['count'] = new_count
                return
            elif now > setted_time:
                del self.IP_DICT[ip_name]
                return
            # 访问次数大于3次，并且当前访问时间小于超时时间。剩余时间访问给用户
            elif new_count > 3 and now <= setted_time:
                delta = setted_time-now
                msg = f'<h1 style="text-align:center;color:red">对不起，您的手速太快了，请{delta.seconds}秒后再试</h1>'
                return HttpResponse(msg)

        else:
            self.IP_DICT.setdefault(ip_name,{'count':0,
                                            'time': datetime.datetime.now()+
                                            datetime.timedelta(minutes=1)
                                            })
            return






    def process_response(self, request, response):

        print("我是MD2类中的process_response方法")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        print("我是MD2类中的process_view方法")


    def process_exception(self, request, exception):
        print("我是MD2类中的process_exception方法")




