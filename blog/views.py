from django.shortcuts import render
from django.views import generic

# Create your views here.

class BlogIndex(generic.ListView):
	queryset = models.Entry.objects.published()
	template_name= "home.html"
	paginate_by = 2