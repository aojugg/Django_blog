from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world")

#def index(request):
#    return HttpResponse(u"欢迎光临， aojugg 博客.")
