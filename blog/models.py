from django.db import models
from django.contrib.auth.models import User

from hadrian.utils import slugs
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

from .managers import PostManager


class Post(models.Model):
    title = models.CharField(blank=False, max_length=450)
    slug = models.SlugField(unique=True)
    image = models.ImageField(blank=True, upload_to='blog/images', null=True)
    body = RichTextField()
    excerpt = models.TextField(blank=True, null=True)
    meta_description = models.CharField(blank=True, max_length=350, help_text='Meta Description for SEO')
    author = models.ForeignKey(User)
    published_date = models.DateTimeField()
    published = models.BooleanField()

    tags = TaggableManager()

    objects = PostManager()

    def __unicode__(self):
        return self.title

    @property
    def get_author_display(self):
        return "%s %s" % (self.author.first_name, self.author.last_name)

    def save(self, *args, **kwargs):
        slugs.unique_slugify(self, self.title)
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('post_detail_view', {}, {'slug': self.slug})

