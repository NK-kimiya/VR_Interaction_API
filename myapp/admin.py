from django.contrib import admin
from .models import CustomModel

class CustomModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', '_password')  # Adminサイトのリスト表示で表示するフィールド
    search_fields = ('name',)  # 検索ボックスで検索できるフィールド
    readonly_fields = ('id',)  # 編集不可のフィールド

admin.site.register(CustomModel, CustomModelAdmin)

