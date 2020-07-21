from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        #models.pyで宣言した変数名しか扱えない。
        fields = ('title', 'text',)


