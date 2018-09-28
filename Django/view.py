from django.http import HttpResponse
# from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")


def world(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)



def search_get(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'

    context = {}
    context['q'] = message
    return render(request, 'get.html', context)

# 接收POST请求数据
def search_post(request):
    if request.POST:
        return HttpResponse(request.POST['q'])
    return HttpResponse("没有内容")