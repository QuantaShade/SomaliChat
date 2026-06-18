from django.shortcuts import render, redirect, get_object_or_404
from .models import Content
from .forms import ContentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def signUp(r):
    form = UserCreationForm()
    if r.method == 'POST':
        form = UserCreationForm(r.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(r, 'app/signUp.html', context)
    
def signIn(r):
    form = AuthenticationForm()
    if r.method == 'POST':
        form = AuthenticationForm(r, r.POST)
        if form.is_valid():
            user = form.get_user()
            login(r, user)
            return redirect("/")
    context = {
        "form": form
    }
    return render(r, 'app/signIn.html', context)
    
def signOut(r):
    if r.method == 'POST':
        logout(r)
        return redirect("/")
    return render(r, 'app/signOut.html')

def home(r):
    content = Content.objects.all().order_by("-postedAt")
    context = {
        'data': content
    }
    return render(r, 'app/home.html', context)

@login_required
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

@login_required
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

@login_required
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