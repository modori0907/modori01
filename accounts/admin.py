from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm
from .models import Students, Schools

User = get_user_model()

class CustomizeUserAdmin(UserAdmin):  #  管理画面の表示しかたをへんこするやり方
    form = UserChangeForm  # ユーザー編集画面で使うForm
    add_form = UserCreationForm  # ユーザー作成画面

    list_display = ('username', 'email', 'is_staff')  #　一覧画面で表示する要素を定期

    #  ユーザー編集画面で表示する要素,UserChangeFormを含める必要がある
    fieldsets = (
        ('ユーザー情報', {'fields': ('username', 'email', 'password', 'website', 'picture')}),
        ('パーミッション', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )

    #  ユーザー作成画面で表示する要素を定義する

    add_fieldsets = (
        ('ユーザー情報', {
            'fields': ('username', 'email', 'password', 'confirm_password')
        }),
    )

admin.site.register(User, CustomizeUserAdmin) # ユーザーを管理画面に表示する。定義した内容を画面に兵頭するため
# admin.site.register(Students)
admin.site.register(Schools)

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):

    fields = ('name', 'score', 'age', 'school') #順番を変更する

    list_display = ('id', 'name', 'age', 'score', 'school')  # 一覧画面で表示する内容を変更する
    #  idのリンクから他の項目をリンクにする方法
    list_display_links = ('name',)


