from django.shortcuts import render
from django.utils import timezone
from .models import Post
#Page not Found 404 Error lol
from django.shortcuts import render, get_object_or_404

def post_list(request):
    #並べ替え　ここでもするの？
    #この 変数 posts を使って、クエリセットのデータにアクセスする。だからかな。毎回整えて取得みたいな
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #htmlテンプレートを組み合わせるrender関数で得た値をreturn
    #リクエストというのは、インターネットを介してユーザから受け取った全ての情報が詰まったもの
    #{} の中に引数を記述する時は、名前と値をセットにしなくてはなりません
    return render(request, 'blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
    #if there is no page,its pk number, then return Error404
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',{'post': post})

