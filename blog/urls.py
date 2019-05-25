from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("update/<int:pk>/", views.PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>/", views.PostDeleteView.as_view(), name="post_delete"),
    path("drafts/", views.DraftListView.as_view(), name="post_draft_list"),
    path("publish/<int:pk>/", views.post_publish, name="post_publish"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("delete/comment/<int:pk>/", views.delete_comment, name="comment_delete"),
]