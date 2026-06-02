from django.urls import path
from .views import home, contentPost, viewContent

urlpatterns = [
    path('', home),
    path('content/post/', contentPost, name='createContent'),
    path('content/details/<int:id>', viewContent, name='viewContent')
]