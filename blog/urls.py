from django.conf.urls import patterns, include, url

from .views import PostDetailView, PostListView, MonthArchive, SearchListView

urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='post_list_view'),
    url(r'^search/$', SearchListView.as_view(), name='post_search_view'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>[-\w]+)/$', MonthArchive.as_view(), name="archive_month"),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name="post_detail_view"),
)