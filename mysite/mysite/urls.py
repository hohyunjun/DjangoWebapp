"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url
from lotto import views

urlpatterns = [
    url(r'^polls/',include('polls.urls')),
    url(r'^admin/',admin.site.urls),
    url(r'^lotto/$', views.index, name='lotto'),
    url(r'^$', views.index, name='index'),
    url(r'^lotto/new/$', views.post, name='new_lotto'),
    #url에서 view로 전달할  lottokey parameter 전달
    url(r'^lotto/(?P<lottokey>[0-9]+)/detail/$', views.detail, name='detail'),
]
