from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



from .models import Post, Author, Comment
from .forms import PostForm, CommentForm

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]   
    return None


class AboutView(TemplateView):
    template_name = "about.html"


class PostListView(ListView):
    queryset = Post.objects.filter(published_at__lte=timezone.now()).order_by("-timestamp")
    template_name = "index.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "post_create.html"

    def form_valid(self, form):
        author = get_author(self.request.user)
        form.instance.author = author
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "post_create.html"

    def form_valid(self, form):
        author = get_author(self.request.user)
        form.instance.author = author
        return super().form_valid(form)


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy("blog:index")
    template_name = "confirm_delete_post.html"


class DraftListView(ListView):
    queryset = Post.objects.filter(published_at__isnull=True).order_by("-timestamp")
    template_name = "drafts.html"
    context_object_name = "drafts"









    
