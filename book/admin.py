from django.contrib import admin
from .models import Book, Review

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description')
    search_fields = ['title', 'description']
    list_editable = ('description','title')#可以看到简介的具体内容,并进行修改其内容

admin.site.register(Book,BookAdmin)#注册book页面
admin.site.register(Review)

