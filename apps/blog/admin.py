from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from blog.models import Article


class ArticleAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
