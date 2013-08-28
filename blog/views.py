from django.views.generic import ListView, DetailView, MonthArchiveView
from django import forms

from .models import Post


class ListMixin(object):
    paginate_by = 5
    context_object_name = 'posts'
    template_name = 'blog/post_list_view.html'

    def get_queryset(self):
        tag = self.request.GET.get('tag', None)
        if tag:
            return Post.objects.published().filter(tags__name__in=[tag])
        return Post.objects.published()


class MonthArchive(ListMixin, MonthArchiveView):
    date_field = 'published_date'


class PostListView(ListMixin, ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail_item.html'


class SearchListView(ListView):
    model = Post
    template_name = 'blog/post_list_view.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        search = self.kwargs.get('q', None)
        if search:
            return Post.objects.published().search(search)
        return Post.objects.all()

