from django.urls import path

from . import views

urlpatterns = [

    # 用户注册函数视图
    path('users/register/',views.register),


# #     用户注册类视图
#     path('users/register/',views.RegisterView.as_view),

]