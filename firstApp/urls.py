from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # CRUD operations on bookk model

    path('create-book', views.createBook, name='create-book'),
    path('read-books', views.readBooks, name='read-books'),
    path('read-books/<str:pk>', views.readOneBook, name='read-one-book'),
    path('update-book/<str:pk>', views.updateBook, name='update-book'),
    path('delete/<str:pk>', views.deleteBook, name='delete-book')

]
