from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    #並べ替え　ここでもするの？
    #この 変数 posts を使って、クエリセットのデータにアクセスする。だからかな。毎回整えて取得みたいな
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #htmlテンプレートを組み合わせるrender関数で得た値をreturn
    #リクエストというのは、インターネットを介してユーザから受け取った全ての情報が詰まったもの
    #{} の中に引数を記述する時は、名前と値をセットにしなくてはなりません
    return render(request, 'blog/post_list.html',{'posts': posts})
