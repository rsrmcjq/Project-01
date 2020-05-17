from django.urls import path,re_path

from . import views

urlpatterns = [

    # # 用户注册函数视图
    # path('users/register/',views.register),


#     用户注册类视图
#     http://127.0.0.1:8000/users/register/
    path('users/register/',views.RegisterView.as_view()),
#     re_path()中没有封装正则表达式的固定规则
#    http://127.0.0.1:8000/users/login/
    re_path(r'^users/login/$',views.LoginView.as_view()),





]