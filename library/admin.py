from django.contrib import admin
from .models import Book 
admin.site.site_header = 'Library Admin'
admin.site.site_title = 'Library Admin Area'
admin.site.index_title = 'Welcome to the Library admin area'
admin.site.register(Book)
