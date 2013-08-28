from django.contrib import admin


from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'published_date')
    fields = (('title', 'slug'), 'image', 'body', ('published_date', 'published'), 'tags')
    prepopulated_fields = {'slug':('title',),}
    save_on_top = True
    date_hierarchy = 'published_date'
    list_filter = ('published',)
    actions = ['publish', 'unpublish']
    search_fields = ('title',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    def publish(self, request, queryset):
        rows = queryset.update(published=True)
        if rows == 1:
            message_bit = "1 blog post was"
        else:
            message_bit = "%s blog posts were" % rows
        self.message_user(request, "%s successfully published." % message_bit)

    def unpublish(self, request, queryset):
        rows = queryset.update(published=False)
        if rows == 1:
            message_bit = "1 blog post was"
        else:
            message_bit = "%s blog posts were" % rows
        self.message_user(request, "%s successfully un-published." % message_bit)

admin.site.register(Post, PostAdmin)