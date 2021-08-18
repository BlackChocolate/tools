from django.http import HttpResponse

from testModel.models import Test


def hello(request):
    return HttpResponse("Hello world ! ")

def testdb(request):
    test1=Test(name='runnoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")