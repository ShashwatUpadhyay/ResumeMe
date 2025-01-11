from django.contrib import admin
from .models import Blog, Comment
# Register your models here.


# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'created_at', 'is_published', 'views']
#     list_filter = ['is_published', 'created_at']
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}
#     date_hierarchy = 'created_at'
#     ordering = ['is_published', 'created_at']
#     actions = ['make_published', 'make_unpublished']
    
#     def make_published(self, request, queryset):
#         queryset.update(is_published=True)
#     make_published.short_description = 'Mark selected blogs as published'

#     def make_unpublished(self, request, queryset):  
#         queryset.update(is_published=False)
#     make_unpublished.short_description = 'Mark selected blogs as unpublished'
    
# admin.site.register(Blog, BlogAdmin)
admin.site.register(Blog)
admin.site.register(Comment)