# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
import redis

def index(request):
    return render(request,"home.html")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def code(request):
    num=0
    telephone= request.GET['a']
    # r=redis.Redis(host='47.93.90.103',port=6379,db=1)
    pool=redis.ConnectionPool(host='47.93.90.103',port=6379,db=1,password="000000")
    r=redis.Redis(connection_pool=pool)

    try:
        key_value="futures:portal:message:captcha:bind:"+telephone
        result=r.mget(key_value)[0]
        code=result
        print code
    except Exception:
        return HttpResponse("未能获取到redis中的验证码，请刷新重试 ")

    # reload()
    return  HttpResponse(str(code))

def codes(request):
    num=0
    telephone= request.GET['a']
    r=redis.Redis(host='47.93.90.103',port=6379,db=1)
    pool=redis.ConnectionPool(host='47.93.90.103',port=6379,db=1,password="000000")
    r=redis.Redis(connection_pool=pool)

    try:
        key_value="futures:portal:message:captcha:bind:"+telephone
        result=r.mget(key_value)[0]
        code=result
        print code
    except Exception:
        return HttpResponse("未能获取到redis中的验证码，请刷新重试 ")

    # reload()
    return  HttpResponse(str(code))