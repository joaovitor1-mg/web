from django.views.generic import ListView, DetailView
from blog.models import Post

class PostListView(ListView):
    model               = Post
    template_name       = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-data_publicacao')

class PostDetailView(DetailView):
    model         = Post
    template_name = 'post_detail.html'