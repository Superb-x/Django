from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from .models import Students
from .forms import UploadFileForm
import pymysql, json, os




def index(request):
    context = {'latest_question_list': 'sub'}
    return render(request, 'forms/index.html', context)

def result(request):
    return render(request, 'forms/result.html', {'foo': 'bar'})

def vote(request):
    print(request)
    print(request.POST)

    student_name = request.POST['name']
    student_sex = request.POST['sex']
    student_school = request.POST['school']
    student_company = request.POST['company']
    student_tel = request.POST['tel']
    student_info = Students.objects.get(id=1)
    print(student_info)
    s1 = Students(
        Name=student_name,
        Sex=student_sex,
        School=student_school,
        Company=student_company,
        Tel=student_tel,
    )
    s1.save()
    return HttpResponseRedirect(reverse('index'))

def search(request):
    return render(request, 'forms/search.html', {'foo': 'bar'})

def list(request):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        charset='utf8mb4',
        password='root',
        database='ftms',
    )
    print(request.POST)
    pos = '%' + request.POST['shop'] + '%'
    cur = conn.cursor()
    cur.execute("SELECT * FROM yc_dealer WHERE city OR province LIKE '%s'" % pos)
    shoparr = []

    for x in cur:
        if x[4].find('<br>') >= 0:
            t = x[4].split('<br>')
        else:
            t = x[4]
        tmp = {'name': x[1], 'tel': t, 'address': x[11]}
        shoparr.append(tmp)
    context = {'list': shoparr}

    cur.close()
    conn.close()
    print(json.dumps(shoparr, ensure_ascii=False))
    return render(request, 'forms/dealerlist.html', context)
    #return HttpResponse(json.dumps(shoparr, ensure_ascii=False), content_type='application/json; charset=utf-8')

def upload(request):
    return render(request, 'forms/upload.html', {'image': 'img7.jpg'})

def uploaded(request):
    if request.method == 'POST':
        myFile = request.FILES.get('img', None)
        if not myFile:
            return HttpResponse('没有上传任何文件')
        dest = open(os.path.join(os.path.dirname(__file__) + '/static/forms/images', myFile.name), 'wb+')
        for chunk in myFile.chunks():
            dest.write(chunk)
        dest.close()

    return HttpResponse('上传成功')