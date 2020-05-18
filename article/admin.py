from django.contrib import admin

from .models import Article,Comment

# Register your models here.
admin.site.register(Comment)

@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ["title","author","created_date","id"]
    list_display_links = ["author","created_date","title"]
    search_fields = ["title","context"]
    list_filter = ["created_date"]
    class Meta:
        model = Article



