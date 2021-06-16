from django.urls import path
from . import views
from myblog.views import CategoryDelete, PostDetail, PostCreate, CategoryList, MyView, CategoryDetail, CategoryCreate, CategoryUpdate, SimpleFormView, welcome


urlpatterns=[
    path("", views.home, name='home'),
    path('view/',MyView.as_view()),
    path('categories',CategoryList.as_view(), name='category_list'),
    path('category/detail/<pk>/', CategoryDetail.as_view(),name='category_detail'),
    path('create/category', CategoryCreate.as_view(), name='category_create'),
    path('category/update/<pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<pk>/',CategoryDelete.as_view(), name='category_delete'),
    path("simple/form", SimpleFormView.as_view(), name="simple_form"),
    path('welcome', views.welcome, name='welcome'),
    path('posts', views.posts,name="posts"),
    path('post/detail/<pk>/', PostDetail.as_view(),name='post_detail'),
    path('create/post', PostCreate.as_view(), name='post_create'),


]