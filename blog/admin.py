from django.contrib import admin
from . import models

#from django_markdown import MarkdownModelAdmin
#from django_markdown.admin import MarkdownModelAdmin
#django markdown doesn't work

#class PostAdmin(MarkdownModelAdmin):
class PostAdmin(admin.ModelAdmin):

	list_display = ['title', 'created']
	prepopulated_fields = {"slug": ("title", )}

admin.site.register(models.Post, PostAdmin)