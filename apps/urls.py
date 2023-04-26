from django.urls import path
from .views import (BookListApiView,book_list_view,
                    BookDetailApiView,BookUpdateApiView,
                    BookDeleteApiView,BookCreateApiView,
                    BookListCreateApiView,BookDetailUpdateDeleteApiView)


urlpatterns=[
    path('',BookListApiView.as_view()),
    path('create/',BookCreateApiView.as_view()),
    path('<int:pk>/',BookDetailApiView.as_view()),
    path('<int:pk>/delete',BookDeleteApiView.as_view()),
    path('<int:pk>/update',BookUpdateApiView.as_view()),
    path('list-create/',BookListCreateApiView.as_view()),
    path('<int:pk>/detail-update-delete/',BookDetailUpdateDeleteApiView.as_view()),
]