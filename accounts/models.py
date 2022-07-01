from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):  #　普通のユーザーを作成するときに呼び出される
        if not email:
            raise ValueError('Enter Email!')
        user = self.model(
            username=username,
            email=email
            #  これ以外はデフォルトの設定が与えられる
        )
        user.set_password(password)   # パスワードを暗号化して保存する
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):  # スーパーユーザーを作成するときに呼び出されるメソッド
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user





class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) #  管理画面のアクセス設定。
    website = models.URLField(null=True)
    picture = models.FileField(null=True)
    #  パスワードはすでにAbstractBaseUserで定義されているのでここで、定義する必要はない.スーパーユーザーも書く必要がない
    USERNAME_FIELD = 'email'# このテーブルのレコードを一意に識別する通常はusernameを識別子にしているが今回はメールアドレスにする変更を行う。そのための設定
    REQUIRED_FIELDS = ['username']# スーパーユーザー作成時に入力するもの。一緒に定義したいもの

    objects = UserManager()

    def __str__(self):
        return self.email  # 管理画面で利用する


class Students(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    score = models.IntegerField()
    school = models.ForeignKey(
        'Schools', on_delete=models.CASCADE
    )



    class Meta:
        db_table = 'students'
        verbose_name_plural = '生徒'
        ordering = ('score',)

    def __str__(self):
        return self.name + ':' + str(self.age)


class Schools(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'schools'
        verbose_name_plural = '学校'

    def __str__(self):
        return self.name


