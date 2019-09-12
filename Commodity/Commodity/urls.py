"""Commodity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from commodities import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pageA1),
    path('pageA1/', views.pageA1),
    path('pageA11/', views.pageA11),
    path('pageA2/', views.pageA2),
    path('pageA3/', views.pageA3),
    path('pageB/', views.pageB),
    path('pageC/', views.pageC),

    # 使用正则进行静态路由
    # 传入图片主码，调出选择的图片，刷新页面
    re_path("find-(?P<page_id>\d+)-(?P<img_id>\d+)", views.find),
    re_path("find_category-(?P<category_id>\d+)", views.find_category)
]
