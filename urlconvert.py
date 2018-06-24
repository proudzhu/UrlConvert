#-*- coding:utf-8 -*-

#功能:迅雷地址转换
#包含：
#输入原始地址 -> 真实地址
#输入原始地址 -> 迅雷地址
#输入原始地址 -> 快车地址
#输入原始地址 -> 旋风地址

import base64
import sys

try:
    import urllib.request, urllib.parse, urllib.error
except ImportError:
    import urllib

PY3 = sys.version_info[0] >= 3

def StrToBase64(s):
    if PY3:
        return base64.b64encode(s.encode('gbk'))
    else:
        return base64.b64encode(s)

def Base64ToStr(b):
    if PY3:
        return base64.b64decode(b).decode('gbk')
    else:
        return base64.b64decode(b)

def StrToBase64str(s):
    if PY3:
        return StrToBase64(s).decode('gbk')
    else:
        return StrToBase64(s)

#解析迅雷地址
def Thunderdecode(url):
    url = url.replace('thunder://','')
    thunderUrl = Base64ToStr(url)[2:-2]
    return thunderUrl

#解析快车地址
def Flashgetdecode(url):
    url=url.replace('Flashget://','')
    if '&' in url:
        url = url.split('&')[0]
    url = Base64ToStr(url)
    flashgeturl = url.replace('[FLASHGET]','')
    flashgeturl=flashgeturl.replace('[FLASHGET]','')
    return flashgeturl

#解析QQ旋风地址
def qqdecode(url):
    url=url.replace('qqdl://','')
    qqurl=Base64ToStr(url)
    return qqurl

#生成迅雷链接
def ThunderEncode(url):
    t_url = "thunder://"+StrToBase64str("AA"+url+"ZZ")
    return t_url

#生成快车链接
def flashetencode(url):
    f_url='Flashget://'+StrToBase64str('[FLASHGET]'+url+'[FLASHGET]')+'&1926'
    return f_url

#生成QQ旋风链接
def qqencode(url):
    q_url='qqdl://'+StrToBase64str(url);
    return q_url;


def urlconvert(oldurl):
    oldurl = oldurl.strip()
    if oldurl == '':
        print('输入错误.')
    elif 'thunder://' in oldurl:
        newurl = Thunderdecode(oldurl) #将迅雷地址解析为真实地址
    elif 'Flashget://' in oldurl: #解析快车地址
        newurl=Flashgetdecode(oldurl)
    elif 'qqdl://' in oldurl: #解析旋风地址
        newurl = qqdecode(oldurl)
    else:
        newurl = oldurl

    thunderurl=ThunderEncode(newurl)
    flashgeturl=flashetencode(newurl)
    qqurl=qqencode(newurl)
    print(newurl)
    print(thunderurl)
    print(flashgeturl)
    print(qqurl)
    
    # ttt = ("&nbsp;&nbsp;&nbsp;<a href='javascript://' onclick='ConvertURL2FG(\""+flashgeturl+"\",\""+newurl+"\",1926)'></a>")
    # print ttt

def main(argv):
    if len(argv) == 1:
        s = [
            'ed2k://|file|%E8%B6%8A%E7%8B%B1.Prison.Break.S05E06.%E4%B8%AD%E8%8B%B1%E5%AD%97%E5%B9%95.HDTVrip.720P.mp4|485576874|9d5a883b071aa5b938410580b56388ea|h=twaamvlskb7xymdfd27vl45kqlo3b7xk|/',
            'thunder://QUFmdHA6Ly95Z2R5ODp5Z2R5OEB5ZzQyLmR5ZHl0dC5uZXQ6ODAwMS9b0fS54rXn07B3d3cueWdkeTguY29tXS4uyfq7r86ju/qjutbV1cIuQkQuNzIwcC65+tOiy6vT7y7W0NOiy6vX1sS7Lm1rdlpa'
            ]
    else:
        s = argv[1:]

    for url in s:
        urlconvert(url)
        print("")

if __name__ == '__main__':
    main(sys.argv)
