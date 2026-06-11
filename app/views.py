from django.shortcuts import render, redirect, get_object_or_404
from .models import Content
from .forms import ContentForm

# Create your views here.

def home(r):
    content = Content.objects.all().order_by("-postedAt")
    context = {
        'data': content
    }
    return render(r, 'app/home.html', context)

def contentPost(r):
    form = ContentForm()
    if r.method == "POST":
        form = ContentForm(r.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {
        'form' : form
    }
    return render(r, 'components/contentPostDialog.html', context)

def contentEdit(r, id):
    content = get_object_or_404(Content, id=id)
    form = ContentForm(instance=content)
    if r.method == "POST":
        form = ContentForm(r.POST, instance=content)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {
        'content': content,
        'form' : form
    }
    return render(r, 'components/contentPostDialog.html', context)

def contentDelete(r, id):
    content = get_object_or_404(Content, id=id)
    content.delete()
    return redirect("/")

def viewContent(r, id):
    content = get_object_or_404(Content, id=id)
    context = {
        "content": content
    }
    return render(r, 'app/viewContent.html', context)