from django.conf.urls.defaults import patterns, include, url
from django.views.generic import dates

from blog.models import Article
from blog.feeds import LatestArticlesFeed

urlpatterns = patterns('',
    url(r'$^',
        dates.ArchiveIndexView.as_view(**{
            'date_field': 'published_at',
            'model': Article}),
    name='home'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        dates.DateDetailView.as_view(**{
            'date_field': 'published_at',
            'model': Article,
            'month_format': '%m'}),
    name='article_detail'),

    url(r'^feed/$', LatestArticlesFeed(), name='feed'),
)