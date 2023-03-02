from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('play',views.play, name='play'),
    path('myfavorite',views.myfavorite, name='myfavorite'),
    path('board',views.board, name='board'),
    path('boardcontent',views.boardcontent, name='boardcontent'),
    path('write',views.write, name='write'),
    path('write_ok',views.write_ok, name='write_ok'),
    path('delete',views.delete, name='delete'),
    path('update',views.update, name='update'),
    path('update_ok/<int:id>',views.update_ok, name='update_ok'),
    path('top_login__',views.top_login, name='top_login__'),
    path('login_ok',views.login_ok, name='login_ok'),
    path('top_join',views.top_join, name='top_join'),
    path('join_ok',views.join_ok, name='join_ok'),
    path('logout_',views.logout,name='logout_'),
    path('top_rank',views.top_rank,name='top_rank'),
    path('addFavor',views.addFavor, name='addFavor'),
    path('deleteFavor',views.deleteFavor,name='deleteFavor'),
    path('search',views.search,name='search'),
    path('search_movie',views.search_movie,name='search_movie'),
]
