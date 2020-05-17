from django.urls import path
from . import views


urlpatterns = [
# 测试提取查询字符串参数：http://127.0.0.1:8000/querystring/?name=zxc&age=18
    path('querystring/',views.QSParamView.as_view()),

    path('formdata/',views.FormDataParamView.as_view()),

    path('json/',views.JSONParamView.as_view()),

    # path('url_param1/18/',views.URLParam1View.as_view()),
    path('url_param1/<int:num>/',views.URLParam1View.as_view()),

    path('url_param2/<mobile:phone_num>/',views.MOBParam1View.as_view()),



]