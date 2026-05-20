from django.shortcuts import render, redirect
from .models import Content

# Create your views here.

def home(request):
    content = Content.objects.all().order_by("-postedAt")
    context = {
        'data': content
    }
    if request.method == "POST":
        title = request.POST.get('title')
        img = request.POST.get('img')
        content = Content.objects.create(
            title = title,
            img = img
        )
        content.save()
        return redirect("/")
    return render(request, 'app/home.html', context)

def about(request):
    return render(request, 'app/about.html')