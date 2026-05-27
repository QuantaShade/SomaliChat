from django.urls import path
from .views import home, contentPost

urlpatterns = [
    path('', home),
    path('content/post/', contentPost, name='createContent')
]