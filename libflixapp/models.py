from django.db import models

class Member(models.Model):
    email = models.EmailField(primary_key=True)
    pwd = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    rdate = models.DateField()
    def __str__(self) :
        return self.nickname

class NoticeBoard(models.Model):
    postname = models.CharField(max_length=70)
    contents = models.TextField()
    password = models.CharField(max_length=50)
    writer = models.ForeignKey('Member', on_delete=models.CASCADE)
    rdate = models.DateTimeField()
    def __str__(self):
        return self.postname
    
class Movies(models.Model):
    title = models.TextField()
    opdate = models.TextField()
    grade = models.TextField()
    genre = models.TextField()
    director = models.TextField()
    rtime = models.TextField()
    movieurl = models.TextField()
    moviethum = models.TextField()

