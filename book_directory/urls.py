from django.urls import path

from . import views

app_name = "book_directory"
urlpatterns = [
    path('', views.index, name='index'),
]
