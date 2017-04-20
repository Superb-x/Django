import re, urllib.request, urllib

def download_img(url):
    try:
        request = urllib.request.Request(url)
        res = urllib.request.urlopen(request)
        data = res.read()
    except Exception:
        res = urllib.request.urlopen('https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&quality=80&size=b150_150&subsize=20480&cut_x=0&cut_w=0&cut_y=0&cut_h=0&sec=1369815402&srctrace&di=84043b37bab12c50faff5f3a0cc8b529&wh_rate=null&src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2Faec379310a55b319380291c141a98226cefc178e.jpg')
        data = res.read()
    return data
def getImg(html):
    reg = r'<img src="(.*?)"'
    pattern = re.compile(reg)
    imgList = re.findall(pattern, repr(html))
    num = 1
    print(imgList)
    for img in imgList:
        image = download_img(img)
        with open('img/%s.jpg' % num, 'wb') as fp:
            fp.write(image)
            num += 1
            print('正在下载第%s张图片' % num)

    return

url = 'http://tieba.baidu.com/f?kw=%C0%EE%D2%E3&fr=ala0&tpl=5'
html = download_img(url)
print(getImg(str(html)))