from django.contrib import admin
# from blog.models import Post
from .models import Post

# Register your models here.
@admin.register(Post) # decorator alternative to admin.site.register()
class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_date' # adds a date drill-down navigation bar at the top

    empty_value_display='-empty-' # shows this text when a field has no value

    list_display=("title", "counted_views", "status", "published_date", "created_date") # columns shown in the list view

    # fields = ("title",) # limits which fields appear in the edit form

    list_filter=("status",) # adds a filter sidebar by status field

    # ordering = ("created_date",)  # ascending  => oldest post first
    # ordering=("-created_date",) # sorts by created_date descending (newest first)

    search_fields=("title", "content") # enables search box filtering by title and content

# admin.site.register(Post, PostAdmin) # makes Post model visible in Django admin panel
