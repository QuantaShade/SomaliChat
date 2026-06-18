from django.urls import path
from .views import home, contentPost, viewContent, contentEdit, contentDelete, signUp, signIn, signOut

urlpatterns = [
    path('', home),
    path('signUp/', signUp),
    path('signIn/', signIn),
    path('signOut/', signOut),
    path('content/post/', contentPost, name='createContent'),
    path('content/details/<int:id>', viewContent, name='viewContent'),
    path('content/update/<int:id>', contentEdit, name='editContent'),
    path('content/delete/<int:id>', contentDelete, name='deleteContent')
]