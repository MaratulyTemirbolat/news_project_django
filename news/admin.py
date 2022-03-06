from django.utils.safestring import mark_safe
from django.contrib import admin

from .models import News
from .models import Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at',
                    'is_published', 'category', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'content',
              'photo', 'created_at', 'views_number', 'updated_at',
              'is_published', 'get_photo')
    # Поля, которые нужны для вывода внутри самой новости ('fields')
    readonly_fields = ('get_photo', 'views_number', 'created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="150">')
        return '-'
    get_photo.short_description = 'Миниатюра'
    # С помощью этого сво-ва у методов можно дать описание методов


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
