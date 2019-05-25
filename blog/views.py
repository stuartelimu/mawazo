from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Post, Author, Comment, PostView
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


class PostDetailView(View):
    form_class = CommentForm
    template_name = "post_detail.html"
    
    
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        PostView.objects.get_or_create(user=request.user, post=post)
        comments = Comment.objects.all().order_by("-timestamp")
        form = self.form_class()
        return render(request, self.template_name, {'post':post, 'form':form, 'comments':comments})

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        PostView.objects.get_or_create(user=request.user, post=post)
        comments = Comment.objects.all().order_by("-timestamp")
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse_lazy("blog:post_detail", kwargs={
                "pk": post.pk
            }))
        return render(request, self.template_name, {'post':post, 'form':form, 'comments':comments})
    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "post_create.html"

    def form_valid(self, form):
        author = get_author(self.request.user)
        form.instance.author = author
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "post_create.html"

    def form_valid(self, form):
        author = get_author(self.request.user)
        form.instance.author = author
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")
    template_name = "confirm_delete_post.html"


class DraftListView(LoginRequiredMixin, ListView):
    # queryset = Post.objects.filter(published_at__isnull=True).order_by("-timestamp")
    template_name = "drafts.html"
    context_object_name = "drafts"

    def get_queryset(self):
        self.author = get_author(self.request.user)
        return Post.objects.filter(published_at__isnull=True, author=self.author).order_by("-timestamp")


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect(reverse("blog:post_detail", kwargs={
        "pk": post_pk
    })) 

def post_publish(request, pk):
    post  = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect(reverse("blog:post_detail", kwargs={
        "pk": post.pk    
    }))   









    
