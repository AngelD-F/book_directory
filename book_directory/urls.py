from django.urls import path

from . import views

app_name = "book_directory"
urlpatterns = [
    path('', views.index, name='index'),
    path('addbook/', views.add_book, name='add_book'),
    path('updatebook/<str:pk>/', views.update_book, name='update_book'),
    path('deletebook/<str:pk>/', views.delete_book, name='delete_book'),
]
