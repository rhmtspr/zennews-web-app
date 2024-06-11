from django.contrib import admin
from berita.models import Kategori, Artikel, Comment

# Register your models here.

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ['judul', 'kategori', 'author']
    search_fields = ['judul']

class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "article", "content"]


admin.site.register(Kategori)
admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(Comment, CommentAdmin)