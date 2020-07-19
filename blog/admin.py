from django.contrib import admin
#↓同じ階層にあるmodels.pyからモデルインポート
from .models import Post

admin.site.register(Post)

