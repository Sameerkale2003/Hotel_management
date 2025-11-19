from  django.urls import path
from.views import *

urlpatterns = [
    path("",home,name="home"),
    path("about/",about,name="about"),
    path("history/",history,name="history"),
    path("add_room/",add_room,name='add_room'),
    path("book_now/<int:pk>",book_now,name='book_now'),
    path("add_room/",add_room,name='add_room'),
    path("booking/",booking,name='booking'),
    path("update/<int:pk>",update,name='update'),
    path("delete/<int:pk>",delete,name='delete'),
    path("h_delete/<int:pk>",h_delete,name='h_delete'),
    path("restore/<int:pk>",restore,name='restore')
]
