from django.shortcuts import render
from django.views import View


# Create your views here.
from django import http


# 定义函数视图
def register(request):
    return http.HttpResponse('假设这是一个注册页面')


# # 定义类视图
# class RegisterView(View):
#     # 需要定义和请求方法同名的函数
#     def get(self,request):
#         return http.HttpResponse('这里假装返回一个注册页面')
#
#
#     def post(self,request):
#         return http.HttpResponse('这里假装实现注册逻辑')

