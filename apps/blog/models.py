from datetime import datetime

from django.db import models
from taggit.managers import TaggableManager
from sorl.thumbnail import ImageField

from utils.timestamp_model import BaseTimestampModel


class Article(BaseTimestampModel):

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique_for_date='published_at')

    tease = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()

    published_at = models.DateTimeField()
    is_commentable = models.BooleanField('allow comments')

    image = ImageField(upload_to="blog",
                       help_text="1000 x 400px",
                       blank=True, null=True)

    tags = TaggableManager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.published_at:
            self.published_at = datetime.now()

        super(Article, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('article_detail', None, {
            'year': self.published_at.year,
            'month': self.published_at.strftime('%m'),
            'day': self.published_at.day,
            'slug': self.slug,
        })
