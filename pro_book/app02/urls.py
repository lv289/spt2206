from django.urls import path, re_path
from app02.views import *


urlpatterns = [
    path('index/',index,name='zx_index'),
    path('index/',index,name='press'),
]
