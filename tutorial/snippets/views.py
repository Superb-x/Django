from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.parsers import JSONParser
from .models import Snippet, User
from .serializers import SnippetSerializer

@csrf_exempt
def snippet_list(request):
    '''
    列出所有的代码片段 或者新建一个代码片段
    :param request: 
    :return: 
    '''
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        response = {
            'msg': '成功',
            'status': 200,
            'data': serializer.data
        }
        return JsonResponse(response, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    '''
    重构、删除、更新一个代码片段
    :param request: 
    :param pk: 
    :return: 
    '''
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        response = {
            'msg': '成功',
            'status': 200,
            'data': serializer.data
        }
        return JsonResponse(response)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
# 这儿装饰器的意思你大概也能明白   忽略csrf保护机制
@csrf_exempt
def register(request):
    # 限定请求方式  要求必须是POST请求
    if request.method == 'GET':
        res = {
            'status': 403,
            'msg': '请求类型错误'
        }
        return JsonResponse(res)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        try:
            nickname = request.POST['nickname']
            idcard = request.POST['idcard']
        except:
            data = {
                'status': 403,
                'msg': '缺少字段'
            }
            return JsonResponse(data, safe=False)
        exist = User.objects.filter(username=username)
        # 如果在当前数据库中存在这个用户名则提示
        if exist:
            return JsonResponse({'status': 403, 'msg': '该用户名已存在'})
        else:
            # 将明文密码做加密处理
            pwd = make_password(password)
            user = User.objects.create(username=username, password=pwd, nickname=nickname, idcard=idcard)
            user.save()
            return JsonResponse({'status': 200, 'msg': '注册成功!'})
# 登录接口
@csrf_exempt
def login(request):
    print(request)
    if request.method == 'GET':
        return JsonResponse({'status': 403, 'msg': '请求类型错误'})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        pwd = User.objects.filter(username=username).values('password')
        pwd = list(pwd)[0]['password']
        if check_password(password, pwd):
            print('成功')
            data = {
                'status': 200,
                'msg': '登录成功',
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'status': 403, 'msg': '用户名或密码输入有误!'}, safe=False)