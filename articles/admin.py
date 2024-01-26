from django.contrib import admin
from .models import Article,Comment

# Register your models here.

class CommentInline(admin.TabularInline): # new
    model = Comment
    extra=0
    
class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
    CommentInline,
    ]


admin.site.register(Comment)
admin.site.register(Article,ArticleAdmin)