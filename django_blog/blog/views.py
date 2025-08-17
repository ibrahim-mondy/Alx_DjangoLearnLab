from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content", "author"]

    def get_success_url(self):
        return reverse_lazy("post_list")

class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]

    def get_success_url(self):
        return reverse_lazy("post_list")

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
