from django.shortcuts import render
from django.utils import timezone
from .models import Post
#Page not Found 404 Error lol
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

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

def post_new(request):

    #Saveボタンをクリックされたとき（のみ、メソッドがPOSTなってる
    if request.method == "POST":
        #requesut.POSTに、入力されたフォームのすべてのフィールドが入ってる
        form = PostForm(request.POST)

        #不正な値がないかチェックする関数 dorm.is_valid()
        if form.is_valid():

            #ポストの前にフォームとして保存 TrueだとPostモデルがauthor追加前に保存されちゃうので明示して止める必要がある
            post = form.save(commit=False)

            #今回はtitleとtextでauthorがないから、ここで必ず記載
            post.author = request.user
            #投稿前に公開日決めちゃうのは、ほんとはよろしくない？？　下書き保存じゃないしいいんでね
            post.published_date = timezone.now()
            # where is save directory??  ・・No,here is the Database[SQLite3],perhaps!!
            post.save()
            return redirect('post_detail', pk=post.pk)

    ##それ以外はなにもしてない（？）→わかった、POST以外のリクエストが来た時。つまり、プラスボタン押されたときやmethodが不正な値の時。は、ErrorExceptとかもなしに、真っ新で真っ白な編集画面戻る。
    # forms.pyのクラスだ！これ。PostForm()  →大元はmodels.pyからきてる！タイトルと内容みたいなフィールドの要素とか
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form':form})


def post_edit(request, pk):
    #関数を読んだページ番号から、ポストモデルを読み込み。
    post = get_object_or_404(Post, pk=pk)

    #saveボタンclickの時（リクエストのメソッド名がポストの時。htmlのメソッドはただのタグ・・？）
    if request.method == "POST":
        # instanceって引数取るのがちょっと謎。2つめの引数の記述がforms.pyにない。公式のModelFormみてみないと「？」だわ
        #ただまぁ、元々の情報に加えて「新しいフィールドの内容？」とかを、足してる処理だとは思う。なんとなく理解。
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            #直ぐに保存しないように？かく   Trueだとあとでするpost.saveも一緒にされちゃうイメージ
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk-post.pk)

    #編集するためにただ開いた場合とか、保存以外に呼び出されたとき！　元々の情報のみ、フォームに読み込む！！
    else:
        form =PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    