from django.http import HttpResponse
from django.shortcuts import render

from TestModel.models import Test


def hello(request):
    return HttpResponse("Hello world ! ")

def client(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
        test1 = Test(name=ctx['rlt'])
        test1.save()
        return HttpResponse("%s添加成功",ctx['rlt'])
    else:
        return render(request, "client.html", ctx)

