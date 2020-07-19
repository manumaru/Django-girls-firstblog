from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
#ポストモデルの作成
class Post(models.Model):
    #管理者を外部キーから参照って感じか？
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #キャラクター(チャー)フィールド..読める・・！ 最長200字で指定。オブジェクトに制限かけてるんか
    title = models.CharField(max_length=200)
    #テキストフィールドは制限なしのテキスト用
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #「掲載」関数で日付今に更新　／　ブログ公開メソッドらしい。これが
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #出た、よくわからんやつｗ　stringの時にタイトルを返すってこと？初期化__init__とはどうちゃう？☆
    #呼ぶと、ポストのタイトルのテキストがstgrで帰ってくる関数みたいだが。__で毎回実行でもさせてんのかな？
    def __str__(self):
        return self.title

