from django.db.models import Manager, Q
from django.db.models.query import QuerySet


class PostQuerySet(QuerySet):
    def published(self):
        return self.filter(published=True)

    def search(self, keyword):
        return self.filter(Q(title__contains=keyword) | Q(body__contains=keyword))


class PostManager(Manager):
    def get_query_set(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_query_set().published()

    def search(self, keyword):
        return self.get_query_set().search(keyword)
        
    def get_latest(self):
        return self.published().latest('published_date')