from django.urls import path
from AuthorBook import views

urlpatterns = [
    path('author/create', views.AuthorCreateApi.as_view(), name= "author_create"),
    path('author/delete', views.AuthorDelete.as_view(), name= "author_delete"),
    path('author/update', views.AuthorUpdateApi.as_view(), name= "author_update"),
    path('author/list', views.AuthorListApi.as_view(), name= "author_list"),

    path('book/create', views.BookCreateApi.as_view(), name= "author_create"),
    path('book/delete', views.BookDelete.as_view(), name= "author_delete"),
    path('book/update', views.BookUpdate.as_view(), name= "author_update"),
    path('book/list', views.BookListApi.as_view(), name= "author_list"),

]