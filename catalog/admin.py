# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book, Categories, Borrower

admin.site.register(Categories)
admin.site.register(Borrower)
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'borrowed_by', 'borrowed_till')
    list_filter = ('borrowed_by',)


admin.site.register(Book, BookAdmin)
