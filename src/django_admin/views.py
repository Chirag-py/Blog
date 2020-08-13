from django.http import HttpResponse
from django.shortcuts import render


from blog.models import BlogPost



def home_page(request):
	qs = BlogPost.objects.all()[:5]
	context = {'blog_list': qs}
	return render(request, 'home.html', context)


