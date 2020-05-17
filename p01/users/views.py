from django.shortcuts import render
# 导入类视图中的父类View
from django.views import View


# Create your views here.
from django import http


# # =====================定义函数视图==============
# def register(request):
#     return http.HttpResponse('假设这是一个注册页面')

# =======================定义类视图================

# class 类名（View）:
#   def 跟请求方法同名的函数名（self,request）:
#         return 响应对象


# 定义注册类视图
class RegisterView(View):
    # 需要定义和请求方法同名的函数
    def get(self,request):
        return http.HttpResponse('这里假装返回一个注册页面')


    def post(self,request):
        return http.HttpResponse('这里假装实现注册逻辑')


# 定义用户登录类视图
class LoginView(View):
    def get(self,request):
        return http.HttpResponse('这里是一个登录页面')


