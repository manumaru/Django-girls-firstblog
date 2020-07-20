from django.shortcuts import render

def post_list(request):
    #htmlテンプレートを組み合わせるrender関数で得た値をreturn
    return render(request, 'blog/post_list.html',{})