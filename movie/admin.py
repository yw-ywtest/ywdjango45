from django.contrib import admin
# Register your models here.
from .models import Movie,Review

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description')
    search_fields = ['title', 'description']
    list_editable = ('description','title')#可以看到简介的具体内容,并进行修改其内容
admin.site.register(Movie)#站点注册movie模型
admin.site.register(Review)