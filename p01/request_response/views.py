from django.shortcuts import render
from django.views import View
from django import http
import json

class QSParamView(View):

    def get(self,request):
        # request.GET专门用于提取请求地址中的查询字符串参数
        name = request.GET.get('name')
        age = request.GET.get('age')
        print(name,age)

        return http.HttpResponse('测试提取查询字符串参数')

class FormDataParamView(View):

    def post(self,request):
        username = request.POST.get('username')
        passward = request.POST.get('passward')
        print(username,passward)

        return http.HttpResponse('测试提取表单类型数据')



class JSONParamView(View):

    def post(self,request):
        origin_data = request.body
        # loads将原始json数据转成Python字典
        json_dict = json.loads(origin_data)

        username = json_dict.get('username')
        password = json_dict.get('password')
        print(username,password)

        return http.HttpResponse('测试提取非表单类型数据')



class URLParam1View(View):

    def get(self,request,num):

        print(num)
        return http.HttpResponse('测试提取url路径数字参数')


class MOBParam1View(View):

    def get(self, request, phone_num):
        print(phone_num)
        return http.HttpResponse('测试提取url路径手机号码参数')

# Create your views here.
