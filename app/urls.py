from django.urls import path
from .views import home, contentPost, viewContent, contentEdit, contentDelete

urlpatterns = [
    path('', home),
    path('content/post/', contentPost, name='createContent'),
    path('content/details/<int:id>', viewContent, name='viewContent'),
    path('content/update/<int:id>', contentEdit, name='editContent'),
    path('content/delete/<int:id>', contentDelete, name='deleteContent')
]