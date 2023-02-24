from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from . models import NoticeBoard, Member,Movies
import datetime
from django.http import JsonResponse

def index(request):
    if  request.session.get('login_') is not None:
        return render(request,'index.html')
    else:
        request.session['nick'] = ""
        request.session['button_name'] = "로그인"
        request.session['button_dir'] = 'top_login__'
        return render(request,'index.html')

def play(request):
    x=request.GET['first']
    print(x)
    res_data={}
    res_data['movies']=Movies.objects.get(title=x)
    return render(request,'play.html',res_data)
    
def myfavorite(request):
    return render(request,'myfavorite.html')

def board(request):
    res_data={}
    res_data['postlist']=NoticeBoard.objects.all()
    return render(request,'board.html',res_data)

def boardcontent(request):
    x = request.GET['list_id']
    res_data={}
    res_data['content']=NoticeBoard.objects.get(id=x)
    return render(request,'boardcontent.html',res_data)

def write(request):
    return render(request,'write.html')

def write_ok(request):
    x = request.POST['title']
    y = request.POST['textfield']
    pwd = request.POST['pwd']
    nowDatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pwd = pwd
    NoticeBoard(postname=x,contents=y,password=pwd,rdate=nowDatetime,writer=Member.objects.get(email=request.session['login_'])).save()
    return redirect('/libflixapp/board')

def delete(request):
    x = request.GET['delete_']
    NoticeBoard.objects.get(id=x).delete()
    return redirect('board')

def update(request):
    x = request.GET['update_']
    res_data={}
    res_data['update_content']=NoticeBoard.objects.get(id=x)
    return render(request,'update.html',res_data)

def update_ok(request,id):
    update_=NoticeBoard.objects.get(id=id)
    x = request.POST['title']
    y = request.POST['textfield']
    pwd = request.POST['pwd']
    nowDatetime = datetime.datetime.now().strftime('%Y-%m-%d')
    update_.postname=x
    update_.contents=y
    update_.password=pwd
    update_.rdate=nowDatetime
    update_.save()
    return redirect('/libflixapp/board')

def login_ok(request):
    x = request.POST['email']
    y = request.POST['pwd']
    # res_data={}
    try:
        login_=Member.objects.get(email=x)
        if login_.pwd== y:
            request.session['login_'] = login_.email
            request.session['nick'] = login_.nickname
            request.session['button_name'] = "로그아웃"
            request.session['button_dir'] = "logout_"
            return redirect('index')
        else:
            pass
            # res_data['error']="비밀번호가 틀렸습니다."
            # return render(request,'top_login.html',res_data)
    except:
        pass
        # res_data['error']="아이디가 없습니다."
        # return render(request,'top_login.html',res_data)


def top_login(request):
    res_data={}
    res_data['member']=Member.objects.all().values()
    return render(request,'top_login.html',res_data)

def top_join(request):
    x=request.GET['urls']
    res_data={}
    res_data['url']=x
    res_data['member']=Member.objects.all().values()
    return render(request,'top_join.html',res_data)

def join_ok(request):
    email_ = request.POST['email']
    pwd_ = request.POST['pwd']
    pwd_check = request.POST['pwd_check']
    nick = request.POST['nick']
    birth = request.POST['birth']
    Member(email=email_, pwd=pwd_, nickname=nick, rdate=birth).save()
    return redirect('index')

def logout(request):
    if request.session.get('login_'):
        del(request.session['login_'])
    return redirect('index')  

def genre(request):
    return render(request,'genre.html')

def top_rank(request):
    return render(request,'top_rank.html')

def top(request):
    if  request.session.get('login_') is not None:
        return render(request,'index.html')
    else:
        request.session['nick'] = ""
        request.session['button_name'] = "로그인"
        request.session['button_dir'] = "top_login"
        return render(request,'index.html')
    
def logout(request):
    if request.session.get('login_'):
        del(request.session['login_'])
        return redirect('./')
