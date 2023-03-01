from django.contrib import admin
from . models import NoticeBoard,Member,Movies,MyFavoriteList,MyViewingHistory

admin.site.register(NoticeBoard)
admin.site.register(Member)
admin.site.register(Movies)
admin.site.register(MyFavoriteList)
admin.site.register(MyViewingHistory)
