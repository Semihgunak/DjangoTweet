from django.contrib import admin
from template_app.models import Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fields =['nickname','message']




admin.site.register(Tweet,TweetAdmin)