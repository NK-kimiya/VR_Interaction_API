from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # カスタムユーザーモデルのフィールドを追加するための設定
    model = CustomUser
    list_display = ['username', 'avatart_number','userid']
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('userid',)}),  # 'userid' を追加
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('userid',)}),  # 'userid' を追加
    )

# カスタムユーザーモデルを管理サイトに登録
admin.site.register(CustomUser, CustomUserAdmin)


