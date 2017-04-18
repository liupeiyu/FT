"""zqxt_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from calc import views as calc_views


urlpatterns = [
    url(r'^$', calc_views.index, name='index'),

    url(r'^add/$', calc_views.add, name='add'),
    url(r'^new_add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
    url(r'^admin/', admin.site.urls),
    url(r'^code/$', calc_views.code,name='code'),
    url(r'^codes/$', calc_views.codes,name='codes'),
]
