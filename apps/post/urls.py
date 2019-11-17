from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('<str:slug>', views.PostDetailView.as_view(), name='post-detail')
]
