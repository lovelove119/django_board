from django.db import models

# Create your models here.
# models.py의 클래스와 DB의 table과 sync를 맞춰 테마를(컬럼정보) 자동생성.

# 클래스명 = 테이블명, 변수=컬럼명
class Test(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # DB에는 fk를 설정한 변수명에 _id가 붙게 된다.
    # on_update = models.CASCADE,
    # db에 fk에 author_id는 파이썬에서는 author객체와 같은것.
    Author = models.ForeignKey(Author,on_delete = models.SET_NULL ,null=True, related_name= 'posts')

