from django.shortcuts import render, redirect
from . models import NoticeBoard, Member,Movies,MyFavoriteList ,MyViewingHistory
import datetime


def index(request):
    res_data={}
    if  request.session.get('login_') is not None:
        res_data['movie_info_action']=Movies.objects.filter(genre='액션').all()
        res_data['movie_info_comedy']=Movies.objects.filter(genre='코미디').all()
        res_data['movie_info_horror']=Movies.objects.filter(genre='공포').all()
        res_data['movie_info_sf_fan']=Movies.objects.filter(genre='SF/판타지').all()
        res_data['movie_info_roman']=Movies.objects.filter(genre='로맨스').all()
        res_data['movie_info_ani']=Movies.objects.filter(genre='애니메이션').all()
        res_data['movie_viewd']=[]
        for x in MyViewingHistory.objects.filter(email=request.session.get('login_')):
            res_data['movie_viewd'].append(Movies.objects.get(id=x.moive_num_id))
        return render(request,'index.html',res_data)
    else:
        request.session['nick'] = ""
        request.session['button_name'] = "Login"
        request.session['button_dir'] = 'top_login__'
        res_data['movie_info_action']=Movies.objects.filter(genre='액션').all()
        res_data['movie_info_comedy']=Movies.objects.filter(genre='코미디').all()
        res_data['movie_info_horror']=Movies.objects.filter(genre='공포').all()
        res_data['movie_info_sf_fan']=Movies.objects.filter(genre='SF/판타지').all()
        res_data['movie_info_roman']=Movies.objects.filter(genre='로맨스').all()
        res_data['movie_info_ani']=Movies.objects.filter(genre='애니메이션').all()
        res_data['movie_viewd']=[]
        for x in MyViewingHistory.objects.filter(email=request.session.get('login_')):
            res_data['movie_viewd'].append(Movies.objects.get(id=x.moive_num_id))
        return render(request,'index.html',res_data)

def play(request):
    x=request.GET['first']
    res_data={}
    res_data['my_viewed_movie']=MyViewingHistory.objects.filter(email=request.session.get('login_'))
    res_data['viewd']=[]
    for i in res_data['my_viewed_movie']:
        res_data['viewd'].append(Movies.objects.get(pk=i.moive_num_id).title)
    if x not in res_data['viewd']:
        MyViewingHistory(email_id=request.session.get('login_'), moive_num_id=Movies.objects.get(title=x).pk).save()
    elif x in res_data['viewd']:
        MyViewingHistory.objects.get(moive_num_id=Movies.objects.get(title=x).pk,email_id=request.session.get('login_')).delete()
        MyViewingHistory(email_id=request.session.get('login_'), moive_num_id=Movies.objects.get(title=x).pk).save()
    else:
        pass
    movie_count=Movies.objects.get(title=x)
    movie_count.count +=1
    movie_count.save()
    res_data['movies']=Movies.objects.get(title=x)
    return render(request,'play.html',res_data)
    
def myfavorite(request):
    try:
        res_data={}
        res_data['my_movie']=MyFavoriteList.objects.filter(email=request.session.get('login_'))
        res_data['favor']=[]
        for i in res_data['my_movie']:
            res_data['favor'].append(Movies.objects.get(id=i.moive_num_id))
        return render(request,'myfavorite.html',res_data)
    except:
        return render(request,'myfavorite.html',res_data)
        

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
    if request.session.get('login_'):
        return render(request,'write.html')
    else:
        return top_login(request)
        
def write_ok(request):
    x = request.POST['title']
    y = request.POST['textfield']
    nowDatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    NoticeBoard(postname=x,contents=y,rdate=nowDatetime,writer=Member.objects.get(email=request.session['login_'])).save()
    return redirect('/libflixapp/board')

def delete(request):
    x = request.GET['delete_']
    y = NoticeBoard.objects.get(id=x)
    if request.session.get('login_') != y.writer_id:
        res_data={}
        res_data['error']='안됨'
        res_data['content']=y
        return render(request,'boardcontent.html',res_data)
    else:
        NoticeBoard.objects.get(id=x).delete()
        return redirect('board')

def update(request):
    res_data={}
    x = request.GET['update_']
    y=NoticeBoard.objects.get(id=x)
    if request.session.get('login_') != y.writer_id:
        res_data['error']='안됨'
        res_data['content']=y
        return render(request,'boardcontent.html',res_data)
    else:
        res_data['update_content']=y
        return render(request,'update.html',res_data)

def update_ok(request,id):
    update_=NoticeBoard.objects.get(id=id)
    x = request.POST['title']
    y = request.POST['textfield']
    nowDatetime = datetime.datetime.now().strftime('%Y-%m-%d')
    update_.postname=x
    update_.contents=y
    update_.rdate=nowDatetime
    update_.save()
    return redirect('/libflixapp/board')

def login_ok(request):
    x = request.POST['email']
    y = request.POST['pwd']
    try:
        login_=Member.objects.get(email=x)
        if login_.pwd== y:
            request.session['login_'] = login_.email
            request.session['nick'] = login_.nickname
            request.session['button_name'] = "Logout"
            request.session['button_dir'] = "logout_"
            return redirect('index')
        else:
            pass
    except:
        pass

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

def top_rank(request):
    res_data={}
    res_data['movie_info']=Movies.objects.all().order_by('-count')[:5]
    res_data['movie_info2']=zip(Movies.objects.all().order_by('-count')[5:10], [6,7,8,9,10]) 
    return render(request,'top_rank.html',res_data)

def top(request):
    if  request.session.get('login_') is not None:
        return render(request,'index.html')
    else:
        request.session['nick'] = ""
        request.session['button_name'] = "Login"
        request.session['button_dir'] = "top_login"
        return render(request,'index.html')
    
def logout(request):
    if request.session.get('login_'):
        del(request.session['login_'])
        return redirect('./')

def addFavor(request):
    if request.session.get('login_'):
        res_data={}
        res_data['my_movie']=MyFavoriteList.objects.filter(email=request.session.get('login_'))
        res_data['favor']=[]
        x=request.GET['second']
        for i in res_data['my_movie']:
            res_data['favor'].append(Movies.objects.get(pk=i.moive_num_id).title)
        if x not in res_data['favor']:
            MyFavoriteList(email_id=request.session.get('login_'), moive_num_id=Movies.objects.get(title=x).pk).save()
        else:
            pass
        return myfavorite(request)
    else:
        pass

def deleteFavor(request):
    x=request.GET['second']
    MyFavoriteList.objects.filter(email_id=request.session.get('login_'), moive_num_id=Movies.objects.get(title=x).pk).delete()
    return myfavorite(request)

def search(request):
    x=request.GET['q']
    res_data={}
    res_data['postlist']=NoticeBoard.objects.filter(postname__contains=x)
    return render(request,'board.html',res_data)