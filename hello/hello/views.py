from django.http import HttpResponse
from django.shortcuts import render

from hello.TestModel.models import Test


def hello(request):
    return HttpResponse("Hello world ! ")

def client(request):
    ctx={}
    if request.POST:
        insertDB(request.POST['q'])
        ctx['rlt']=request.POST['q']
    return render(request,"client.html",ctx)

def insertDB(content):
    if content is not None:
        print(content)
        test1= Test(name=content)
        test1.save()
# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")