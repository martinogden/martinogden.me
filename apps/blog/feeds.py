from datetime import datetime

from django.contrib.syndication.views import Feed
from blog.models import Article


class LatestArticlesFeed(Feed):
    title = "Latest Articles posted on martinogden.me"
    link = "/feed/"
    description = "Work, ideas, projects, problems, solutions, comment etc."

    def items(self):
        return Article.objects.filter(published_at__lt=datetime.now())[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
