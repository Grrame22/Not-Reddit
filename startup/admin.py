from django.contrib import admin
from .models import (Article, Preferences,
                     UserProfile, ArticleColor, Gender, Comments)

admin.site.register(Article)
admin.site.register(UserProfile)
admin.site.register(Preferences)
admin.site.register(ArticleColor)
admin.site.register(Gender)
admin.site.register(Comments)
