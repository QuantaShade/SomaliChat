from django.shortcuts import render, redirect, get_object_or_404
from .models import Content

# Create your views here.

def home(r):
    content = Content.objects.all().order_by("-postedAt")
    context = {
        'data': content
    }
    return render(r, 'app/home.html', context)

def contentPost(r):
    if r.method == "POST":
        title = r.POST.get('title')
        img = r.POST.get('img')
        content = Content.objects.create(
            title = title,
            img = img
        )
        content.save()
        return redirect("/")
    return render(r, 'components/contentPostDialog.html')

def viewContent(r, id):
    content = get_object_or_404(Content, id=id)
    context = {
        "content": content
    }
    return render(r, 'app/viewContent.html', context)