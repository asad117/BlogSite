from csv import list_dialects
from unicodedata import name
from django.contrib import admin


from blog.models import Post, Tag, Author, Contact, Comment
# Register your models here.
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ("name", "email", "date")

# admin.site.register(Blog, BlogAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "author", "date")
    list_filter = ("tags", "author", "date")
    prepopulated_fields = {"slug":("title",)} 


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "comment", "post")



admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Contact)
admin.site.register(Comment, CommentAdmin)