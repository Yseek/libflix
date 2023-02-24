from django.contrib import admin
from . models import NoticeBoard,Member,Movies,MyFavoriteList

admin.site.register(NoticeBoard)
admin.site.register(Member)
admin.site.register(Movies)
admin.site.register(MyFavoriteList)
