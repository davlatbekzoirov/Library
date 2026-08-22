from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','isbn','price')
    search_fields = ('title','author','isbn','price')
    list_filter = ('author','isbn','price')
    list_per_page = 10

admin.site.register(Book,BookAdmin)