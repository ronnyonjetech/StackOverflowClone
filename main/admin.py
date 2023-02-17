from django.contrib import admin
from .models import *
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','user')
    search_fields=('title','detail')
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(UpVote)
admin.site.register(DownVote)
admin.site.register(Comment)